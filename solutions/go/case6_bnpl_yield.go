package main

import "math"

type BnplYieldCalculator struct {
	DefaultRate   float64
	CostOfCapital float64
}

type BnplResult struct {
	OrderValue          float64 `json:"order_value"`
	MerchantFee         float64 `json:"merchant_fee"`
	ExpectedLoss        float64 `json:"expected_loss"`
	CapitalCost         float64 `json:"capital_cost"`
	NetProfit           float64 `json:"net_profit"`
	NetMarginPct        float64 `json:"net_margin_pct"`
	IsProfitable        bool    `json:"is_profitable"`
}

func NewBnplYieldCalculator(defaultRate, costOfCapital float64) *BnplYieldCalculator {
	return &BnplYieldCalculator{DefaultRate: defaultRate, CostOfCapital: costOfCapital}
}

func (c *BnplYieldCalculator) CalculateNetMargin(orderValue, mdrPct float64, installments int) BnplResult {
	merchantFee := orderValue * (mdrPct / 100.0)
	expectedLoss := orderValue * c.DefaultRate
	capitalCost := orderValue * (c.CostOfCapital / (12.0 / float64(installments)))
	netProfit := merchantFee - (expectedLoss + capitalCost)
	marginPct := (netProfit / orderValue) * 100.0

	return BnplResult{
		OrderValue:   orderValue,
		MerchantFee:  math.Round(merchantFee*100) / 100,
		ExpectedLoss: math.Round(expectedLoss*100) / 100,
		CapitalCost:  math.Round(capitalCost*100) / 100,
		NetProfit:    math.Round(netProfit*100) / 100,
		NetMarginPct: math.Round(marginPct*100) / 100,
		IsProfitable: netProfit > 0,
	}
}
