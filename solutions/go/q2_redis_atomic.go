package main

import (
	"context"

	"github.com/redis/go-redis/v9"
)

const reserveLuaScript = `
local available = tonumber(redis.call('GET', KEYS[1]))
local amount = tonumber(ARGV[1])
if available and available >= amount then
    redis.call('DECRBY', KEYS[1], amount)
    return 1
else
    return 0
end
`

// CreditReservationService handles distributed atomic credit checks via Redis Lua
type CreditReservationService struct {
	rdb *redis.Client
}

func NewCreditReservationService(rdb *redis.Client) *CreditReservationService {
	return &CreditReservationService{rdb: rdb}
}

func (s *CreditReservationService) ReserveCredit(ctx context.Context, accountID string, amount int64) (bool, error) {
	key := "account:" + accountID + ":available_credit"
	res, err := s.rdb.Eval(ctx, reserveLuaScript, []string{key}, amount).Result()
	if err != nil {
		return false, err
	}
	return res.(int64) == 1, nil
}
