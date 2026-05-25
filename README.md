# Quantitative Trading System (Docker-first)

This repo can run entirely in Docker using `docker compose` (no host `pip install` needed).

## 1) Prerequisites
- Docker Engine + Docker Compose v2
- (Optional) existing external PostgreSQL container if you prefer not to use the bundled `postgres` service

## 2) Configure environment + API keys
```bash
cp .env.example .env
# then edit .env
```

Put keys in `.env`:
- `OPENAI_API_KEY` for AI-powered analysis
- `ALPHA_VANTAGE_API_KEY` for Alpha Vantage data
- `BINANCE_API_KEY` + `BINANCE_API_SECRET` for Binance private endpoints
- Binance market endpoint can vary by region/network. Set `BINANCE_TLD` in `.env` if needed (for example: `com` or `us`).

## 3) Database (PostgreSQL) + DDL/DML
This repository now ships PostgreSQL init SQL at:
- `db/init/001_init.sql`

It creates:
- `market_data`
- `trades`
- `signals`
- `performance`

and seeds one default row in `performance` using `ON CONFLICT DO NOTHING`.

### If you already run PostgreSQL in another docker-compose
Set these in `.env` and either:
1. remove/disable the `postgres` service in this repo’s compose, or
2. keep it but change `POSTGRES_PORT` to avoid host-port conflict.

## 4) Start every service with docker-compose
```bash
# build images with all project extras preinstalled
docker compose build

# start postgres + api + dashboard
docker compose up -d

# watch logs
docker compose logs -f api dashboard postgres
```

### Skip the build step (faster local startup)
If you already built images previously (or you only changed mounted source files), you can skip an explicit build:
```bash
# starts services without forcing a rebuild
docker compose up -d
```

If you want Compose to use existing images and fail instead of building missing ones:
```bash
docker compose up -d --no-build
```

### Use `docker-compose.override.yml`
Docker Compose automatically loads `docker-compose.override.yml` when present, so this is enough:
```bash
docker compose up -d
```

To be explicit (or to use a differently named override file), pass files directly:
```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
```

Services:
- API: `http://localhost:8000`
- Streamlit dashboard: `http://localhost:8501`
- PostgreSQL: `localhost:${POSTGRES_PORT:-5432}`

## Dashboard User Guide (Streamlit)

The Streamlit dashboard (`http://localhost:8501`) uses an **explicit apply flow**:

1. In the left sidebar, set:
   - **Date Range**
   - **Strategy**
   - **Symbols**
   - **Initial Capital**
2. Click **🚀 Run Analysis** to apply changes.
3. Review updated outputs across tabs:
   - **Performance Analysis**: equity curve, drawdown, rolling metrics, and summary stats.
   - **Strategy Backtest**: strategy-specific parameters and backtest simulation.
   - **Market Data**: symbol chart, RSI, volume, and quick market stats.
   - **AI Analysis**: sentiment and factor analysis modules.
4. After any sidebar change, click **Run Analysis** again to refresh.

Notes:
- If no symbols are selected, analysis will not run.
- End date must be later than start date.

## 5) Run functional modules (all from containers)

### a) Data Fetching / Data Management
> If you updated the repository recently, rebuild first so new dependencies/scripts are available in the image:
> `docker compose build quantity-api`

```bash
# multi-source public data fetching demo (Binance public endpoints)
docker compose run --rm quantity-api python examples/fetch_public_data.py

# yahoo example (requires yfinance in image; included after rebuild)
docker compose run --rm quantity-api python examples/yahoo_example.py

# real-time websocket chart demo
docker compose run --rm quantity-api python demo_charts_websocket.py
```

### b) Quantitative Analysis / Screening / Optimization
```bash
# factor models + screening + optimization demo
docker compose run --rm quantity-api python examples/factor_analysis_demo.py

# broader quant strategy demo
docker compose run --rm quantity-api python examples/quantitative_strategies.py
```

### c) Strategy Backtesting
```bash
docker compose run --rm quantity-api python examples/extensible_strategy_demo.py
```

### d) AI-Powered Analysis
```bash
# requires OPENAI_API_KEY

docker compose run --rm quantity-api python examples/ai_sentiment_analysis.py

docker compose run --rm quantity-api python examples/langchain_llm_demo.py

docker compose run --rm quantity-api python examples/llm_nlp_complete_demo.py
```

### e) User Interfaces
```bash
# already started via docker compose up -d
# API UI: http://localhost:8000
# Streamlit: http://localhost:8501
```

### f) Tests
```bash
docker compose run --rm quantity-api pytest -q
```

## 6) Validate that the system is "working"
A practical validation path is:
1. `docker compose up -d`
2. Run public data fetch demo successfully.
3. Run factor/strategy examples successfully.
4. Run backtesting demo successfully.
5. Run tests successfully.

If all pass, the repo is operational as a quantitative research/trading framework in containerized mode.

## 7) Stop and cleanup
```bash
docker compose down
# remove DB volume too (destructive)
docker compose down -v
```
