import time
import redis
from fastapi import Request, HTTPException
from app.config import REDIS_HOST, REDIS_PORT, WINDOW, RATE_LIMIT

# Koneksi ke Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


async def rate_limiter(request: Request):
    """Middleware untuk membatasi jumlah request per IP."""
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    # Cek jumlah request dalam window
    current_count = redis_client.get(key)

    if current_count and int(current_count) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

    # Tambahkan request baru
    pipe = redis_client.pipeline()
    pipe.incr(key, 1)
    pipe.expire(key, WINDOW)  # Set waktu kedaluwarsa ke 1 jam
    pipe.execute()
