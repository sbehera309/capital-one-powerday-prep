package main

import (
	"math"
	"sync"
	"time"
)

// RetryPolicy calculates SQS visibility timeout with exponential backoff
type RetryPolicy struct{}

func (r *RetryPolicy) CalculateVisibilityTimeout(retryCount int, baseSeconds int) int {
	return int(math.Pow(2, float64(retryCount)) * float64(baseSeconds))
}

// NotificationCircuitBreaker guards third-party SMS/Email gateway calls
type NotificationCircuitBreaker struct {
	mu                 sync.Mutex
	failureThreshold   int
	recoveryTimeoutSec int64
	failureCount       int
	state              string // "CLOSED", "OPEN", "HALF_OPEN"
	lastFailureTime    int64
}

func NewCircuitBreaker(threshold int, recoverySec int64) *NotificationCircuitBreaker {
	return &NotificationCircuitBreaker{
		failureThreshold:   threshold,
		recoveryTimeoutSec: recoverySec,
		state:              "CLOSED",
	}
}

func (cb *NotificationCircuitBreaker) CanExecute() bool {
	cb.mu.Lock()
	defer cb.mu.Unlock()

	now := time.Now().Unix()
	if cb.state == "OPEN" {
		if now-cb.lastFailureTime > cb.recoveryTimeoutSec {
			cb.state = "HALF_OPEN"
			return true
		}
		return false
	}
	return true
}

func (cb *NotificationCircuitBreaker) RecordResult(success bool) {
	cb.mu.Lock()
	defer cb.mu.Unlock()

	if success {
		cb.failureCount = 0
		cb.state = "CLOSED"
	} else {
		cb.failureCount++
		cb.lastFailureTime = time.Now().Unix()
		if cb.failureCount >= cb.failureThreshold {
			cb.state = "OPEN"
		}
	}
}
