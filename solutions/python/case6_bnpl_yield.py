"""
Capital One PowerDay Engineering Compendium
Case 6: BNPL (Buy-Now-Pay-Later) Cash Flow & Merchant Discount Rate (MDR) Yield Calculator
Language: Python
"""

class BnplYieldCalculator:
    def __init__(self, default_rate: float = 0.025, cost_of_capital: float = 0.04):
        self.default_rate = default_rate          # 2.5% annualized default rate
        self.cost_of_capital = cost_of_capital      # 4.0% interest cost of capital

    def calculate_net_margin(self, order_value: float, mdr_percentage: float, installments: int = 4) -> dict:
        """
        Calculates net unit economics for a 4-installment BNPL loan.
        MDR = Merchant Discount Rate (fee paid by merchant to Capital One, e.g. 3.5%).
        """
        upfront_merchant_fee = order_value * (mdr_percentage / 100.0)
        expected_default_loss = order_value * self.default_rate
        capital_cost = order_value * (self.cost_of_capital / (12 / installments))
        
        net_profit = upfront_merchant_fee - (expected_default_loss + capital_cost)
        net_margin_pct = (net_profit / order_value) * 100.0

        return {
            "order_value": order_value,
            "merchant_fee_collected": round(upfront_merchant_fee, 2),
            "expected_default_loss": round(expected_default_loss, 2),
            "cost_of_capital": round(capital_cost, 2),
            "net_profit": round(net_profit, 2),
            "net_margin_percentage": round(net_margin_pct, 2),
            "is_profitable": net_profit > 0
        }
