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

    hoje = datetime.now().date()
    jogos = []

    for jogo in data.get("matches", []):
        data_jogo = datetime.fromisoformat(jogo["utcDate"].replace("Z", "+00:00")).date()

        if data_jogo >= hoje:
            mandante = jogo["homeTeam"]["name"]
            visitante = jogo["awayTeam"]["name"]
            rodada = jogo.get("matchday", "N/A")

            jogos.append(
                f"📅 Rodada {rodada}\n⚽ {mandante} x {visitante}\n"
            )

    return jogos[:20]
