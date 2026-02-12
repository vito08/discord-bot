import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("API_KEY")

LEAGUE_ID = 71  # Brasileirão Série A
SEASON = 2026
CHANNEL_NAME = "📅agenda-brasileirao"

TEAM_SIGLAS = {
    "spfc": 1, # São Paulo
    "bah": 2, # Bahia
    "rbb": 3, # Red Bull Bragantino
    "cha": 4, # Chapecoense
    "mir": 5, # Mirassol
    "sep": 6, # Palmeiras
    "flu": 7, # Fluminense
    "cor": 8, # Coritiba
    "fla": 9, # Flamengo
    "brf": 10, # Botafogo
    "cap": 11, # Atlético Paranaense
    "gre": 12, # Grêmio
    "vit": 13, # Vitória
    "cam": 14, # Atlético Mineiro
    "rem": 15, # Remo
    "int": 16, # Internacional
    "san": 17, # Santos
    "vdg": 18, # Vasco da Gama
    "cru": 19, # Cruzeiro
    "sccp": 20, # Corinthians
}