import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

# Rate Limiting Settings (Optional)
RATE_LIMIT_STR = os.getenv("RATE_LIMIT")
WINDOW_STR = os.getenv("WINDOW")

RATE_LIMIT = None
WINDOW = None

if RATE_LIMIT_STR is not None:
    try:
        RATE_LIMIT = int(RATE_LIMIT_STR)
    except ValueError:
        raise ValueError("If RATE_LIMIT is set, it must be an integer.")

if WINDOW_STR is not None:
    try:
        WINDOW = int(WINDOW_STR)
    except ValueError:
        raise ValueError("If WINDOW is set, it must be an integer.")

# Redis Configuration (Optional Port)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost") # Default to localhost if not set
REDIS_PORT_STR = os.getenv("REDIS_PORT")

REDIS_PORT = None # Default to None if not set

if REDIS_PORT_STR is not None:
    try:
        REDIS_PORT = int(REDIS_PORT_STR)
    except ValueError:
        raise ValueError("If REDIS_PORT is set, it must be an integer.")

# Optional Redis Password and DB (handle similarly if uncommented)
# REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
# REDIS_DB_STR = os.getenv("REDIS_DB")
# REDIS_DB = None
# if REDIS_DB_STR is not None:
#     try:
#         REDIS_DB = int(REDIS_DB_STR)
#     except ValueError:
#         raise ValueError("If REDIS_DB is set, it must be an integer.")