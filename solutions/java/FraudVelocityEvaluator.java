package com.capitalone.prep;

/**
 * System Design Q4: Real-Time POS Fraud Impossible Travel Velocity
 * Java Solution
 */
public class FraudVelocityEvaluator {

    private static final double EARTH_RADIUS_MILES = 3958.8;

    public double haversineDistanceMiles(double lat1, double lon1, double lat2, double lon2) {
        double dLat = Math.toRadians(lat2 - lat1);
        double dLon = Math.toRadians(lon2 - lon1);
        double rLat1 = Math.toRadians(lat1);
        double rLat2 = Math.toRadians(lat2);

        double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                   Math.cos(rLat1) * Math.cos(rLat2) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return EARTH_RADIUS_MILES * c;
    }

    public boolean isImpossibleTravel(double lat1, double lon1, double ts1Sec,
                                      double lat2, double lon2, double ts2Sec) {
        double timeDiffHours = (ts2Sec - ts1Sec) / 3600.0;
        if (timeDiffHours <= 0) return true;

        double distanceMiles = haversineDistanceMiles(lat1, lon1, lat2, lon2);
        double speedMph = distanceMiles / timeDiffHours;
        return speedMph > 600.0;
    }
}
