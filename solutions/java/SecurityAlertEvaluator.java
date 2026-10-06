package com.capitalone.prep;

/**
 * Case 3: 3-Boolean Security Alert Truth Table & Logic Optimization
 * Java Solution
 */
public class SecurityAlertEvaluator {

    public static boolean shouldFlagTransaction(boolean isForeign, boolean isHighValue, boolean isNewMerchant) {
        return isForeign || (isHighValue && isNewMerchant);
    }
}
