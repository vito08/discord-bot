import requests
from datetime import datetime
from config import API_KEY

def buscar_agenda():
    url = "https://api.football-data.org/v4/competitions/BSA/matches"

    headers = {
        "X-Auth-Token": API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    agora = datetime.now().astimezone()
    jogos = []

    for jogo in data.get("matches", []):

        data_jogo = datetime.fromisoformat(
            jogo["utcDate"].replace("Z", "+00:00")
        )

        data_local = data_jogo.astimezone()

        if data_local.date() >= agora.date():

            mandante = jogo["homeTeam"]["name"]
            visitante = jogo["awayTeam"]["name"]
            rodada = jogo.get("matchday", "N/A")

            data_formatada = data_local.strftime("%d/%m/%Y")
            hora_formatada = data_local.strftime("%H:%M")

            jogos.append(
                f"📅 {data_formatada} às {hora_formatada}\n"
                f"🏆 Rodada {rodada}\n"
                f"⚽ {mandante} x {visitante}\n"
            )

    return jogos[:20]