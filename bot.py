import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN, CHANNEL_NAME, TEAM_SIGLAS
from services.api import buscar_agenda

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Função que posta agenda automaticamente
async def postar_agenda():
    canal = discord.utils.get(bot.get_all_channels(), name=CHANNEL_NAME)

    if not canal:
        return

    jogos = buscar_agenda()

    if jogos:
        mensagem = "📢 **Agenda Brasileirão 2026 (Próximos Jogos)**\n\n"
        mensagem += "\n".join(jogos)
        await canal.send(mensagem)
    else:
        await canal.send("Nenhum jogo futuro encontrado.")


# Comando manual
@bot.command()
async def agenda(ctx, sigla: str = None):

    # Se o usuário digitou uma sigla
    if sigla:
        sigla = sigla.lower()
        time_id = TEAM_SIGLAS.get(sigla)

        if not time_id:
            await ctx.send("❌ Sigla inválida.")
            return

        jogos = buscar_agenda(time_id)
        titulo = f"📢 **Próximos jogos - {sigla.upper()}**\n\n"

    else:
        jogos = buscar_agenda()
        titulo = "📢 **Agenda Brasileirão 2026 (Próximos Jogos)**\n\n"

    if jogos:
        mensagem = titulo + "\n".join(jogos)
        await ctx.send(mensagem)
    else:
        await ctx.send("Nenhum jogo futuro encontrado.")


# Postagem semanal automática
@tasks.loop(hours=168)
async def agenda_semanal():
    await postar_agenda()


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    agenda_semanal.start()


bot.run(DISCORD_TOKEN)
