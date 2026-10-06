package main

import "fmt"

// StorageClient defines the partition range lookup interface
type StorageClient interface {
	RetrieveRange(customerID int64, startTimestamp, endTimestamp int64) ([]string, error)
}

// CustomerDataStore manages real-time customer history retrieval
type CustomerDataStore struct {
	store StorageClient
}

// NewCustomerDataStore initializes the data store with a storage client
func NewCustomerDataStore(client StorageClient) *CustomerDataStore {
	return &CustomerDataStore{store: client}
}

// RetrieveRecent fetches historical customer events using a single partition range query
func (cds *CustomerDataStore) RetrieveRecent(customerID int64, currTime int64, timeWindowMinutes int64) ([]string, error) {
	if timeWindowMinutes <= 0 {
		return []string{}, nil
	}
	startTime := currTime - timeWindowMinutes + 1
	return cds.store.RetrieveRange(customerID, startTime, currTime)
}

func main() {
	fmt.Println("Case 1 Eeno Go implementation ready.")
}
