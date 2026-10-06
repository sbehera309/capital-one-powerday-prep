"""
Capital One PowerDay Engineering Compendium
Case 7: Real-Time Cross-Border FX Settlement & Capital Buffer Engine
Language: Python
"""

class FxSettlementEngine:
    def __init__(self, fx_spread_bps: float = 15.0):
        self.fx_spread_bps = fx_spread_bps  # 15 basis points spread (0.15%)

    def execute_conversion(self, amount_usd: float, spot_rate_eur: float, account_buffer_eur: float) -> dict:
        """
        Executes cross-border USD to EUR conversion with spread pricing and capital buffer check.
        """
        spread_multiplier = 1.0 - (self.fx_spread_bps / 10000.0)
        effective_rate = spot_rate_eur * spread_multiplier
        converted_eur = amount_usd * effective_rate
        
        # Capital buffer check: ensures bank holds sufficient EUR liquidity to settle immediately
        has_sufficient_liquidity = account_buffer_eur >= converted_eur

        return {
            "amount_usd": amount_usd,
            "spot_rate": spot_rate_eur,
            "effective_rate": round(effective_rate, 4),
            "settled_eur": round(converted_eur, 2),
            "fx_fee_usd": round(amount_usd * (self.fx_spread_bps / 10000.0), 2),
            "approved": has_sufficient_liquidity,
            "status": "SETTLED_INSTANT" if has_sufficient_liquidity else "QUEUED_SWIFT_NOSTRO"
        }
