"""
Capital One PowerDay System Design Q6:
Enterprise Notification Engine - Exponential Backoff & Circuit Breaker
Language: Python
"""
import time
import math

class RetryPolicy:
    def calculate_visibility_timeout(self, retry_count: int, base_seconds: int = 5) -> int:
        """
        Calculates SQS Visibility Timeout with Exponential Backoff:
        Visibility Timeout = 2^(retry_count) * 5 seconds
        """
        return int(math.pow(2, retry_count) * base_seconds)

class NotificationCircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout_sec: int = 30):
        self.threshold = failure_threshold
        self.recovery_timeout = recovery_timeout_sec
        self.failure_count = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        self.last_failure_time = 0

    def can_execute(self) -> bool:
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                return True
            return False
        return True

    def record_result(self, success: bool):
        if success:
            self.failure_count = 0
            self.state = "CLOSED"
        else:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.threshold:
                self.state = "OPEN"
