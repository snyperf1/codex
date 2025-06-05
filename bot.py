from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Telegram token loaded:", TELEGRAM_TOKEN is not None)
print("OpenAI API key loaded:", OPENAI_API_KEY is not None)
