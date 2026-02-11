import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN, CHANNEL_NAME
from services.api import buscar_agenda

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def postar_agenda():
    canal = discord.utils.get(bot.get_all_channels(), name=CHANNEL_NAME)
    if canal:
        jogos = buscar_agenda()

        if jogos:
            mensagem = "📢 **Agenda Brasileirão 2026 (Próximos Jogos)**\n\n"
            mensagem += "\n".join(jogos)
            await canal.send(mensagem)
        else:
            await canal.send("Nenhum jogo futuro encontrado.")

@bot.command()
async def agenda(ctx):
    jogos = buscar_agenda()

    if jogos:
        mensagem = "📢 **Agenda Brasileirão 2026 (Próximos Jogos)**\n\n"
        mensagem += "\n".join(jogos)
        await ctx.send(mensagem)
    else:
        await ctx.send("Nenhum jogo futuro encontrado.")

@tasks.loop(hours=168)  # 1 vez por semana
async def agenda_semanal():
    await postar_agenda()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    agenda_semanal.start()

bot.run(DISCORD_TOKEN)