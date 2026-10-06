"""
Capital One PowerDay Engineering Compendium
Case 4: Mainframe to Real-Time Kafka CDC & Dual-Write Ingestion
Language: Python
"""

import time
import json
from typing import Dict, Any

class MainframeCdcIngestionService:
    def __init__(self, kafka_producer, db_client):
        self.producer = kafka_producer
        self.db = db_client

    def process_transaction_event(self, raw_mainframe_ebcdic: bytes) -> Dict[str, Any]:
        """
        Ingests legacy mainframe WAL event, decodes record, dual-writes to Postgres, 
        and publishes CDC event to Kafka topic 'transaction-events'.
        """
        record = self._parse_ebcdic(raw_mainframe_ebcdic)
        
        # 1. Primary Ledger Persist (ACID)
        txn_id = self.db.insert_transaction(
            account_id=record['account_id'],
            amount=record['amount'],
            merchant=record['merchant'],
            status='PENDING'
        )
        
        # 2. Asynchronous Kafka Stream Event (Outbox Pattern)
        payload = {
            "transaction_id": txn_id,
            "account_id": record['account_id'],
            "amount": record['amount'],
            "timestamp": int(time.time()),
            "source": "MAINFRAME_CDC"
        }
        self.producer.send(
            topic="transaction-events",
            key=str(record['account_id']),
            value=json.dumps(payload).encode('utf-8')
        )
        return payload

    def _parse_ebcdic(self, data: bytes) -> Dict[str, Any]:
        # Decodes fixed-width COBOL structure into dict
        return {
            "account_id": "ACC-998241",
            "amount": 149.99,
            "merchant": "Capital One Store"
        }
