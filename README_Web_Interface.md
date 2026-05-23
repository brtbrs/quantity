# Trading System Web Interface

A modern web management interface that provides user-friendly operations for the trading system.

## 🚀 Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation and serialization

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling
- **JavaScript (ES6+)** - Interaction logic
- **Bootstrap 5** - Responsive UI framework
- **Chart.js** - Charting library
- **Boxicons** - Icon library

## 📦 Installation

### 1. Install Dependencies

```bash
# Install all dependencies (including web interface)
pip install -e .[web,ai,visualization]

# Or install web dependencies only
pip install fastapi uvicorn jinja2 aiofiles
```

### 2. Start the Web Interface

```bash
# Method 1: use launcher script
python run_web_interface.py

# Method 2: start FastAPI directly
uvicorn data_service.web.api_server:APIServer().app --host 0.0.0.0 --port 8000 --reload
```

### 3. Access the Interface

Open your browser and visit: http://localhost:8000

## 🎯 Features

### 📊 Dashboard
- **System Status Monitoring** - Real-time system status
- **Performance Metrics** - Total return, Sharpe ratio, max drawdown, etc.
- **Risk Metrics** - VaR, CVaR, Beta, and more
- **Equity Curve** - Interactive return curve chart
- **Portfolio Allocation** - Asset allocation pie chart
- **Recent Activity** - Real-time activity log
- **Recent Trades** - Trade history table

### 🎮 Strategy Management
- **Strategy List** - Display all available strategies
- **Strategy Details** - View config and performance
- **Create Strategy** - Build new strategies via form
- **Start/Stop Controls** - Manage running status
- **Strategy Backtesting** - Run backtests and view results

### 📈 Backtesting
- **Backtest Configuration** - Set backtest parameters
- **Strategy Selection** - Pick strategy to test
- **Time Range** - Configure test period
- **Result Display** - Show metrics and charts

### 💼 Portfolio Management
- **Positions** - View current holdings
- **Portfolio Summary** - Total value, cash, and invested amount
- **PnL Analysis** - Daily and cumulative PnL
- **Weight Allocation** - Asset-level weights

### 🤖 AI Analysis
- **Sentiment Analysis** - Analyze text sentiment
- **Market Analysis** - AI-driven market insights
- **Real-Time Results** - Instant analysis output

## 🔧 API Endpoints

### System Status
```http
GET /api/system/status
```

### Strategy Management
```http
GET /api/strategies
POST /api/strategies
PUT /api/strategies/{id}
DELETE /api/strategies/{id}
POST /api/strategies/{id}/start
POST /api/strategies/{id}/stop
```

### Backtesting
```http
POST /api/backtest/run
```

### AI Analysis
```http
POST /api/ai/analyze
```

### Market Data
```http
GET /api/market/data/{symbol}
```

### Portfolio
```http
GET /api/portfolio/status
```

### Trade History
```http
GET /api/trades/recent
```

## 🎨 UI Screenshots

### Main Dashboard
- System status overview
- Performance metric cards
- Real-time charts
- Activity logs

### Strategy Management
- Strategy card grid
- Strategy detail modal
- Start/stop controls

### Backtest Interface
- Configuration form
- Result display
- Performance charts

## 🔒 Security Features

- **CORS Support** - Cross-origin request handling
- **Input Validation** - Pydantic-based validation
- **Error Handling** - Unified error responses
- **Logging** - Complete operational logs

## 📱 Responsive Design

- **Mobile Support** - Optimized for phones and tablets
- **Desktop Optimization** - Enhanced large-screen layout
- **Touch-Friendly** - Supports touch interactions

## 🚀 Deployment

### Development
```bash
python run_web_interface.py
```

### Production
```bash
# Gunicorn
gunicorn data_service.web.api_server:APIServer().app -w 4 -k uvicorn.workers.UvicornWorker

# Docker
docker build -t trading-system .
docker run -p 8000:8000 trading-system
```

### Reverse Proxy (Nginx)
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🔧 Configuration

### Environment Variables
```bash
export TRADING_SYSTEM_HOST=0.0.0.0
export TRADING_SYSTEM_PORT=8000
export TRADING_SYSTEM_DEBUG=true
```

### Config File
Create `config.json`:
```json
{
    "web": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": false,
        "cors_origins": ["*"]
    },
    "trading": {
        "initial_capital": 100000,
        "commission_rate": 0.001
    }
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Check port usage
   netstat -tulpn | grep 8000

   # Kill process
   kill -9 <PID>
   ```

2. **Missing dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission issues**
   ```bash
   # Linux/Mac
   chmod +x run_web_interface.py

   # Windows
   python run_web_interface.py
   ```

### View Logs
```bash
# Application log
tail -f logs/trading_system.log

# Error log
tail -f logs/error.log
```

## 📈 Performance Optimization

### Frontend Optimization
- Lazy-load charts
- Data caching
- Compress static assets

### Backend Optimization
- Database connection pooling
- Redis caching
- Asynchronous processing

## 🔮 Roadmap

- User authentication and role-based access control
- Multi-account and broker connectivity
- Real-time alerts and notification center
- More advanced analytics dashboards
- One-click strategy deployment and monitoring
