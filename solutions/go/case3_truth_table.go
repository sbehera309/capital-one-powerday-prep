package main

// ShouldFlagTransaction evaluates multi-variable security alert heuristics
// De Morgan's Simplification: returns true if international OR (high value AND new merchant)
func ShouldFlagTransaction(isForeign, isHighValue, isNewMerchant bool) bool {
	return isForeign || (isHighValue && isNewMerchant)
}
