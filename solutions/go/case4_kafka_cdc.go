package main

import (
	"context"
	"encoding/json"
	"time"
)

type Database interface {
	InsertTransaction(accountID string, amount float64, merchant string) (string, error)
}

type KafkaProducer interface {
	Send(topic string, key string, value []byte) error
}

type MainframeCdcService struct {
	db       Database
	producer KafkaProducer
}

type TransactionEvent struct {
	TransactionID string  `json:"transaction_id"`
	AccountID     string  `json:"account_id"`
	Amount        float64 `json:"amount"`
	Timestamp     int64   `json:"timestamp"`
	Source        string  `json:"source"`
}

func NewMainframeCdcService(db Database, producer KafkaProducer) *MainframeCdcService {
	return &MainframeCdcService{db: db, producer: producer}
}

func (s *MainframeCdcService) ProcessTransactionEvent(ctx context.Context, accountID string, amount float64, merchant string) (*TransactionEvent, error) {
	txnID, err := s.db.InsertTransaction(accountID, amount, merchant)
	if err != nil {
		return nil, err
	}

	event := &TransactionEvent{
		TransactionID: txnID,
		AccountID:     accountID,
		Amount:        amount,
		Timestamp:     time.Now().Unix(),
		Source:        "MAINFRAME_CDC",
	}

	payload, err := json.Marshal(event)
	if err != nil {
		return nil, err
	}

	err = s.producer.Send("transaction-events", accountID, payload)
	if err != nil {
		return nil, err
	}

	return event, nil
}
