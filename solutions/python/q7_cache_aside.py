"""
Capital One PowerDay System Design Q7:
Distributed Banking Cache Architecture (Cache-Aside + SETNX Stampede Lock + Read-Your-Own-Writes)
Language: Python
"""
import time
import redis

class CacheAsideManager:
    def __init__(self, redis_client: redis.Redis, db_client):
        self.r = redis_client
        self.db = db_client

    def get_account_balance(self, account_id: str, client_min_version: int = 0) -> dict:
        """
        Retrieves account balance using Cache-Aside with SETNX stampede locking
        and Read-Your-Own-Writes version validation.
        """
        cache_key = f"account:{account_id}:balance"
        lock_key = f"lock:account:{account_id}"

        # 1. Read from Redis Cache
        cached = self.r.hgetall(cache_key)
        if cached and int(cached.get(b"version", 0)) >= client_min_version:
            return {"balance": float(cached[b"balance"]), "version": int(cached[b"version"])}

        # 2. Acquire Mutex Lock to Prevent Cache Stampede
        acquired_lock = self.r.set(lock_key, "LOCKED", nx=True, ex=5)
        if not acquired_lock:
            time.sleep(0.05)  # Wait 50ms and retry read from cache
            return self.get_account_balance(account_id, client_min_version)

        try:
            # 3. Cache Miss / Outdated Version: Query Primary DB
            data = self.db.query_account(account_id)
            # 4. Populate Cache
            self.r.hset(cache_key, mapping={"balance": data["balance"], "version": data["version"]})
            self.r.expire(cache_key, 300)
            return data
        finally:
            self.r.delete(lock_key)
