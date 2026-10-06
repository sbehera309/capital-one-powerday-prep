package main

import "math"

// FraudVelocityEvaluator implements sliding window velocity check for impossible travel
type FraudVelocityEvaluator struct{}

// HaversineDistanceMiles returns distance in miles between coordinates
func (f *FraudVelocityEvaluator) HaversineDistanceMiles(lat1, lon1, lat2, lon2 float64) float64 {
	const R = 3958.8 // Miles
	dLat := (lat2 - lat1) * math.Pi / 180.0
	dLon := (lon2 - lon1) * math.Pi / 180.0
	lat1Rad := lat1 * math.Pi / 180.0
	lat2Rad := lat2 * math.Pi / 180.0

	a := math.Sin(dLat/2)*math.Sin(dLat/2) +
		math.Cos(lat1Rad)*math.Cos(lat2Rad)*math.Sin(dLon/2)*math.Sin(dLon/2)
	c := 2 * math.Atan2(math.Sqrt(a), math.Sqrt(1-a))
	return R * c
}

// IsImpossibleTravel checks if speed between 2 transaction locations exceeds 600 mph
func (f *FraudVelocityEvaluator) IsImpossibleTravel(lat1, lon1, ts1Sec, lat2, lon2, ts2Sec float64) bool {
	timeDiffHours := (ts2Sec - ts1Sec) / 3600.0
	if timeDiffHours <= 0 {
		return true
	}
	dist := f.HaversineDistanceMiles(lat1, lon1, lat2, lon2)
	speedMph := dist / timeDiffHours
	return speedMph > 600.0
}
