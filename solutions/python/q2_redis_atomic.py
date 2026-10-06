"""
Capital One PowerDay System Design Q2:
Credit Limit Concurrent Throttler & Atomic Balance Reservation
Language: Python
"""
import redis

RESERV_LUA_SCRIPT = """
local available = tonumber(redis.call('GET', KEYS[1]))
local amount = tonumber(ARGV[1])
if available and available >= amount then
    redis.call('DECRBY', KEYS[1], amount)
    return 1
else
    return 0
end
"""

class CreditReservationService:
    def __init__(self, redis_client: redis.Redis):
        self.r = redis_client
        self._script = self.r.register_script(RESERV_LUA_SCRIPT)

    def reserve_credit(self, account_id: str, amount: float) -> bool:
        """
        Executes balance validation and decrement atomically inside an embedded Lua script.
        Prevents race conditions when multiple authorized users transact simultaneously.
        """
        key = f"account:{account_id}:available_credit"
        result = self._script(keys=[key], args=[int(amount)])
        return result == 1
