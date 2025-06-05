# Codex Sample Bot

This repository demonstrates a minimal setup for a ChatGPT-powered Telegram bot.

## Project Structure

```
shri-gpt-telegram-bot/
├── bot.py            # Main bot script
├── .env              # Secret keys (not committed)
├── requirements.txt  # Python dependencies
└── README.md         # Project notes
```

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your tokens:
   ```env
   TELEGRAM_BOT_TOKEN=your-botfather-token-here
   OPENAI_API_KEY=your-openai-api-key-here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

The bot will load the tokens from `.env` and confirm that they were loaded successfully.
