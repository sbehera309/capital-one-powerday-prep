"""
Capital One PowerDay Engineering Compendium
Case 2: Virtual Card Generation (Logic Bug Resolution)
Language: Python
"""

def generate_virtual_card(db, user_id: str, expiry_hours: int, is_one_time: bool) -> str:
    """
    Generates dynamic virtual credit card numbers or reuses an existing active card.
    
    Fixes legacy bug where `is_one_time == False` mistakenly forced brand new card creation.
    """
    if is_one_time:
        return db.create_new_card(user_id, ttl_hours=expiry_hours)
    
    existing_card = db.find_active_reusable_card(user_id)
    if existing_card:
        return existing_card
    
    return db.create_new_card(user_id, ttl_hours=None)
