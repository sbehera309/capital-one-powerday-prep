"""
Capital One PowerDay System Design Q4:
Real-Time POS Transaction Ingestion & Impossible Travel Fraud Detection
Language: Python
"""
import math

class FraudVelocityEvaluator:
    @staticmethod
    def haversine_distance_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculates distance between two coordinates in miles using Haversine formula."""
        R = 3958.8  # Earth radius in miles
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def is_impossible_travel(self, lat1: float, lon1: float, ts1_sec: float,
                            lat2: float, lon2: float, ts2_sec: float) -> bool:
        """
        Calculates travel velocity (mph) across sliding window.
        Flags anomaly if velocity > 600 mph.
        """
        time_diff_hours = (ts2_sec - ts1_sec) / 3600.0
        if time_diff_hours <= 0:
            return True  # Zero or negative time diff for non-identical location is impossible
        
        distance_miles = self.haversine_distance_miles(lat1, lon1, lat2, lon2)
        speed_mph = distance_miles / time_diff_hours
        return speed_mph > 600.0
