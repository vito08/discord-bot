import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("API_KEY")

LEAGUE_ID = 71  # Brasileirão Série A
SEASON = 2026
CHANNEL_NAME = "agenda-brasileirao"