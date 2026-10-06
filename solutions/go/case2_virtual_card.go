package main

// CardDB abstracts virtual card storage and retrieval
type CardDB interface {
	CreateNewCard(userID string, ttlHours *int) (string, error)
	FindActiveReusableCard(userID string) (string, error)
}

// GenerateVirtualCard fixes the logic bug to ensure reusable cards are reused properly
func GenerateVirtualCard(db CardDB, userID string, expiryHours int, isOneTime bool) (string, error) {
	if isOneTime {
		return db.CreateNewCard(userID, &expiryHours)
	}

	existingCard, err := db.FindActiveReusableCard(userID)
	if err == nil && existingCard != "" {
		return existingCard, nil
	}

	return db.CreateNewCard(userID, nil)
}
