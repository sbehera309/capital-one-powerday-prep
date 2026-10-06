package com.capitalone.prep;

public class FxSettlementEngine {

    private final double spreadBps;

    public FxSettlementEngine(double spreadBps) {
        this.spreadBps = spreadBps;
    }

    public static class FxResult {
        public final double amountUsd;
        public final double spotRate;
        public final double effectiveRate;
        public final double settledEur;
        public final double fxFeeUsd;
        public final boolean approved;
        public final String status;

        public FxResult(double amountUsd, double spotRate, double effectiveRate, double settledEur, double fxFeeUsd, boolean approved, String status) {
            this.amountUsd = amountUsd;
            this.spotRate = spotRate;
            this.effectiveRate = effectiveRate;
            this.settledEur = settledEur;
            this.fxFeeUsd = fxFeeUsd;
            this.approved = approved;
            this.status = status;
        }
    }

    public FxResult executeConversion(double amountUsd, double spotRateEur, double accountBufferEur) {
        double effectiveRate = spotRateEur * (1.0 - (spreadBps / 10000.0));
        double convertedEur = amountUsd * effectiveRate;
        boolean approved = accountBufferEur >= convertedEur;
        String status = approved ? "SETTLED_INSTANT" : "QUEUED_SWIFT_NOSTRO";

        return new FxResult(
            amountUsd,
            spotRateEur,
            Math.round(effectiveRate * 10000.0) / 10000.0,
            Math.round(convertedEur * 100.0) / 100.0,
            Math.round(amountUsd * (spreadBps / 10000.0) * 100.0) / 100.0,
            approved,
            status
        );
    }
}
