import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

# Rate Limiting Settings
RATE_LIMIT_STR = os.getenv("RATE_LIMIT", "100") # Default to 100 if not set
WINDOW_STR = os.getenv("WINDOW", "3600") # Default to 3600 if not set
try:
    RATE_LIMIT = int(RATE_LIMIT_STR)
    WINDOW = int(WINDOW_STR)
except ValueError:
    raise ValueError("RATE_LIMIT and WINDOW must be integers.")

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost") # Default to localhost
REDIS_PORT_STR = os.getenv("REDIS_PORT", "6379") # Default to 6379
try:
    REDIS_PORT = int(REDIS_PORT_STR)
except ValueError:
    raise ValueError("REDIS_PORT must be an integer.")

# Optional Redis Password and DB (uncomment if needed)
# REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
# REDIS_DB_STR = os.getenv("REDIS_DB", "0")
# try:
#     REDIS_DB = int(REDIS_DB_STR)
# except ValueError: