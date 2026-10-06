package com.capitalone.prep;

public class BnplYieldCalculator {

    private final double defaultRate;
    private final double costOfCapital;

    public BnplYieldCalculator(double defaultRate, double costOfCapital) {
        this.defaultRate = defaultRate;
        this.costOfCapital = costOfCapital;
    }

    public static class Result {
        public final double orderValue;
        public final double merchantFee;
        public final double expectedLoss;
        public final double capitalCost;
        public final double netProfit;
        public final double netMarginPct;
        public final boolean isProfitable;

        public Result(double orderValue, double merchantFee, double expectedLoss, double capitalCost, double netProfit, double netMarginPct, boolean isProfitable) {
            this.orderValue = orderValue;
            this.merchantFee = merchantFee;
            this.expectedLoss = expectedLoss;
            this.capitalCost = capitalCost;
            this.netProfit = netProfit;
            this.netMarginPct = netMarginPct;
            this.isProfitable = isProfitable;
        }
    }

    public Result calculateNetMargin(double orderValue, double mdrPercentage, int installments) {
        double merchantFee = orderValue * (mdrPercentage / 100.0);
        double expectedLoss = orderValue * defaultRate;
        double capitalCost = orderValue * (costOfCapital / (12.0 / installments));
        double netProfit = merchantFee - (expectedLoss + capitalCost);
        double netMarginPct = (netProfit / orderValue) * 100.0;

        return new Result(
            orderValue,
            Math.round(merchantFee * 100.0) / 100.0,
            Math.round(expectedLoss * 100.0) / 100.0,
            Math.round(capitalCost * 100.0) / 100.0,
            Math.round(netProfit * 100.0) / 100.0,
            Math.round(netMarginPct * 100.0) / 100.0,
            netProfit > 0
        );
    }
}
