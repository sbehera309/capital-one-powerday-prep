"""
Capital One PowerDay Engineering Compendium
Case 3: 3-Boolean Security Alert Truth Table & Logic Optimization
Language: Python
"""

def should_flag_transaction(is_foreign: bool, is_high_value: bool, is_new_merchant: bool) -> bool:
    """
    Flags transaction if:
    1. It is an international charge, OR
    2. It is high value AND occurring at an unfamiliar merchant.

    De Morgan's simplification of nested conditional tree.
    """
    return is_foreign or (is_high_value and is_new_merchant)
