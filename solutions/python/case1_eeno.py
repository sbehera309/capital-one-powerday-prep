"""
Capital One PowerDay Engineering Compendium
Case 1: "Eeno" Real-Time Customer History Retrieval & Network Optimization
Language: Python
"""

class CustomerDataStore:
    def __init__(self, storage_client):
        self.store = storage_client

    def retrieve_recent(self, customer_id: int, curr_time: int, time_window_minutes: int) -> list:
        """
        Retrieves historical customer interactions within [curr_time - time_window_minutes + 1, curr_time].
        Replaces O(T) sequential network calls with a single partition range query.
        """
        if time_window_minutes <= 0:
            return []
        start_time = curr_time - time_window_minutes + 1
        return self.store.retrieve_range(
            partition_key=customer_id,
            start_timestamp=start_time,
            end_timestamp=curr_time
        )
