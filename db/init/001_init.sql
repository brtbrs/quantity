DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'quantuser') THEN
        CREATE ROLE quantuser LOGIN PASSWORD 'quantpwd';
    END IF;
END
$$;

CREATE DATABASE quantitydibi OWNER quantuser;

GRANT CONNECT ON DATABASE quantitydibi TO quantuser;

GRANT USAGE ON SCHEMA public TO quantuser;

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO quantuser;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO quantuser;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE ON TABLES TO quantuser;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO quantuser;

CREATE TABLE IF NOT EXISTS market_data (
    id BIGSERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    volume DOUBLE PRECISION,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(symbol, timestamp)
);

CREATE TABLE IF NOT EXISTS trades (
    id BIGSERIAL PRIMARY KEY,
    order_id TEXT UNIQUE,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,
    quantity DOUBLE PRECISION NOT NULL,
    price DOUBLE PRECISION NOT NULL,
    status TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS signals (
    id BIGSERIAL PRIMARY KEY,
    strategy_name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    signal_type TEXT NOT NULL,
    strength DOUBLE PRECISION,
    timestamp TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS performance (
    id BIGSERIAL PRIMARY KEY,
    date DATE NOT NULL UNIQUE,
    total_pnl DOUBLE PRECISION,
    daily_return DOUBLE PRECISION,
    max_drawdown DOUBLE PRECISION,
    sharpe_ratio DOUBLE PRECISION,
    win_rate DOUBLE PRECISION,
    total_trades INTEGER,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO performance (date, total_pnl, daily_return, max_drawdown, sharpe_ratio, win_rate, total_trades) VALUES (CURRENT_DATE, 0, 0, 0, 0, 0, 0) ON CONFLICT (date) DO NOTHING;
