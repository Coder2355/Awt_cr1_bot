# config.py
import os

# Telegram bot token (from BotFather)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7722665729:AAG30JhxFJ5chbGF0WoEGMX6TUfsBfNCT78")  # Replace with your bot's token

# Crunchyroll login credentials (from environment variables or hardcoded if needed)
CRUNCHYROLL_USERNAME = os.getenv("CRUNCHYROLL_USERNAME", "crunchyvera4@tayvstore.com")  # Replace with your username
CRUNCHYROLL_PASSWORD = os.getenv("CRUNCHYROLL_PASSWORD", "storeha315")  # Replace with your password

# Optional: User-Agent for Crunchyroll API
CRUNCHYROLL_USER_AGENT = os.getenv("CRUNCHYROLL_USER_AGENT", "CrunchyrollBot/1.0")

# Paths to DRM decryption tools (set path to mp4decrypt, ffmpeg, and mkvmerge as needed)
MP4DECRYPT_PATH = os.getenv("MP4DECRYPT_PATH", "/path/to/mp4decrypt")  # Adjust this path
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/usr/bin/ffmpeg")  # Adjust this path
MKVMERGE_PATH = os.getenv("MKVMERGE_PATH", "/usr/bin/mkvmerge")  # Adjust this path
