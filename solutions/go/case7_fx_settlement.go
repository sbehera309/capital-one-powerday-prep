package main

import "math"

type FxSettlementEngine struct {
	SpreadBps float64
}

type FxResult struct {
	AmountUSD     float64 `json:"amount_usd"`
	SpotRate      float64 `json:"spot_rate"`
	EffectiveRate float64 `json:"effective_rate"`
	SettledEUR    float64 `json:"settled_eur"`
	FxFeeUSD      float64 `json:"fx_fee_usd"`
	Approved      bool    `json:"approved"`
	Status        string  `json:"status"`
}

func NewFxSettlementEngine(spreadBps float64) *FxSettlementEngine {
	return &FxSettlementEngine{SpreadBps: spreadBps}
}

func (e *FxSettlementEngine) ExecuteConversion(amountUSD, spotRateEUR, bufferEUR float64) FxResult {
	effectiveRate := spotRateEUR * (1.0 - (e.SpreadBps / 10000.0))
	convertedEUR := amountUSD * effectiveRate
	hasLiquidity := bufferEUR >= convertedEUR

	status := "QUEUED_SWIFT_NOSTRO"
	if hasLiquidity {
		status = "SETTLED_INSTANT"
	}

	return FxResult{
		AmountUSD:     amountUSD,
		SpotRate:      spotRateEUR,
		EffectiveRate: math.Round(effectiveRate*10000) / 10000,
		SettledEUR:    math.Round(convertedEUR*100) / 100,
		FxFeeUSD:      math.Round(amountUSD*(e.SpreadBps/10000.0)*100) / 100,
		Approved:      hasLiquidity,
		Status:        status,
	}
}
