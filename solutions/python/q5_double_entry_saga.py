"""
Capital One PowerDay System Design Q5:
Peer-to-Peer Payment Double-Entry Ledger & Saga Pattern (Zelle/Venmo)
Language: Python
"""

class PeerToPeerLedger:
    def __init__(self, db_connection):
        self.conn = db_connection

    def transfer_funds_saga(self, tx_id: str, sender_acc: str, receiver_acc: str, amount: float) -> bool:
        """
        Executes double-entry bookkeeping with strict row locking (SELECT FOR UPDATE).
        Inserts immutable paired DEBIT and CREDIT ledger entries.
        """
        cursor = self.conn.cursor()
        try:
            # Lock sender row & verify balance
            cursor.execute("SELECT balance FROM accounts WHERE account_id = %s FOR UPDATE;", (sender_acc,))
            row = cursor.fetchone()
            if not row or row['balance'] < amount:
                self.conn.rollback()
                return False

            # Insert Debit and Credit ledger entries atomically
            cursor.execute("""
                INSERT INTO ledger_entries (entry_id, transaction_id, account_id, amount, currency, entry_type)
                VALUES 
                  (gen_random_uuid(), %s, %s, %s, 'USD', 'DEBIT'),
                  (gen_random_uuid(), %s, %s, %s, 'USD', 'CREDIT');
            """, (tx_id, sender_acc, -amount, tx_id, receiver_acc, amount))
            
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            raise e
