import requests
from datetime import datetime, timedelta
from config import API_KEY, LEAGUE_ID, SEASON

BASE_URL = "https://v3.football.api-sports.io/fixtures"


def buscar_agenda(time_id=None):
    headers = {
        "x-apisports-key": API_KEY
    }

    params = {
        "league": LEAGUE_ID,
        "season": SEASON,
        "status": "NS"
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return []

    dados = response.json()
    jogos = []

    for jogo in dados["response"]:

        if time_id:
            if (
                jogo["teams"]["home"]["id"] != time_id and
                jogo["teams"]["away"]["id"] != time_id
            ):
                continue

        data_utc = datetime.fromisoformat(
            jogo["fixture"]["date"].replace("Z", "+00:00")
        )

        data_brasil = data_utc - timedelta(hours=3)

        data_formatada = data_brasil.strftime("%d/%m")
        hora_formatada = data_brasil.strftime("%H:%M")

        mandante = jogo["teams"]["home"]["name"]
        visitante = jogo["teams"]["away"]["name"]

        # Layout diferente se for por time
        if time_id:
            mensagem = f"{data_formatada} • {hora_formatada} — {mandante} x {visitante}"
        else:
            rodada = jogo["league"]["round"]
            mensagem = (
                f"📅 {data_formatada}/{data_brasil.year} às {hora_formatada}\n"
                f"🏟 {mandante} x {visitante}\n"
                f"🎯 {rodada}\n"
            )

        jogos.append(mensagem)

    if not jogos:
        return []

    if time_id:
        return jogos[:5]

    return jogos[:20]
