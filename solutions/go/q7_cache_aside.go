package main

import (
	"context"
	"strconv"
	"time"

	"github.com/redis/go-redis/v9"
)

type DBClient interface {
	QueryAccount(accountID string) (float64, int64, error)
}

// CacheAsideManager implements cache-aside pattern with stampede protection in Go
type CacheAsideManager struct {
	rdb *redis.Client
	db  DBClient
}

func NewCacheAsideManager(rdb *redis.Client, db DBClient) *CacheAsideManager {
	return &CacheAsideManager{rdb: rdb, db: db}
}

func (c *CacheAsideManager) GetAccountBalance(ctx context.Context, accountID string, clientMinVersion int64) (float64, int64, error) {
	cacheKey := "account:" + accountID + ":balance"
	lockKey := "lock:account:" + accountID

	val, err := c.rdb.HMGet(ctx, cacheKey, "balance", "version").Result()
	if err == nil && val[0] != nil && val[1] != nil {
		ver, _ := strconv.ParseInt(val[1].(string), 10, 64)
		if ver >= clientMinVersion {
			bal, _ := strconv.ParseFloat(val[0].(string), 64)
			return bal, ver, nil
		}
	}

	// Stampede Lock via SetNX
	locked, err := c.rdb.SetNX(ctx, lockKey, "LOCKED", 5*time.Second).Result()
	if err != nil || !locked {
		time.Sleep(50 * time.Millisecond)
		return c.GetAccountBalance(ctx, accountID, clientMinVersion)
	}
	defer c.rdb.Del(ctx, lockKey)

	bal, ver, err := c.db.QueryAccount(accountID)
	if err != nil {
		return 0, 0, err
	}

	c.rdb.HSet(ctx, cacheKey, "balance", bal, "version", ver)
	c.rdb.Expire(ctx, cacheKey, 5*time.Minute)
	return bal, ver, nil
}
