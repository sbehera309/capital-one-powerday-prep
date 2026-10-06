package main

import (
	"context"
	"database/sql"
	"errors"
)

// PeerToPeerLedger executes ACID double-entry transactions in PostgreSQL
type PeerToPeerLedger struct {
	db *sql.DB
}

func NewPeerToPeerLedger(db *sql.DB) *PeerToPeerLedger {
	return &PeerToPeerLedger{db: db}
}

func (l *PeerToPeerLedger) TransferFunds(ctx context.Context, txID, senderAcc, receiverAcc string, amount float64) error {
	tx, err := l.db.BeginTx(ctx, &sql.TxOptions{Isolation: sql.LevelReadCommitted})
	if err != nil {
		return err
	}
	defer tx.Rollback()

	var balance float64
	err = tx.QueryRowContext(ctx, "SELECT balance FROM accounts WHERE account_id = $1 FOR UPDATE", senderAcc).Scan(&balance)
	if err != nil {
		return err
	}
	if balance < amount {
		return errors.New("insufficient funds")
	}

	query := `
		INSERT INTO ledger_entries (entry_id, transaction_id, account_id, amount, currency, entry_type)
		VALUES 
		  (gen_random_uuid(), $1, $2, $3, 'USD', 'DEBIT'),
		  (gen_random_uuid(), $1, $4, $5, 'USD', 'CREDIT');
	`
	_, err = tx.ExecContext(ctx, query, txID, senderAcc, -amount, receiverAcc, amount)
	if err != nil {
		return err
	}

	return tx.Commit()
}
