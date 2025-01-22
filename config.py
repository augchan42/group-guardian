from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables with type casting and defaults
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))  # Default 0 for error checking
API_HASH = os.getenv("API_HASH")
SPOILER_MODE = os.getenv("SPOILER_MODE", "True").lower() == "true"  # String to bool conversion

# Validation
if not all([BOT_TOKEN, API_ID, API_HASH]):
    raise ValueError("Missing required environment variables. Please check your .env file.")