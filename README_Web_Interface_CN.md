# Trading System Web Interface

一个现代化的Web管理界面，为交易系统提供用户友好的操作界面。

## 🚀 技术栈

### 后端 (Backend)
- **FastAPI** - 高性能的Python Web框架
- **Uvicorn** - ASGI服务器
- **Pydantic** - 数据验证和序列化

### 前端 (Frontend)
- **HTML5** - 语义化标记
- **CSS3** - 现代化样式
- **JavaScript (ES6+)** - 交互逻辑
- **Bootstrap 5** - 响应式UI框架
- **Chart.js** - 图表库
- **Boxicons** - 图标库

## 📦 安装

### 1. 安装依赖

```bash
# 安装所有依赖（包括Web界面）
pip install -e .[web,ai,visualization]

# 或者单独安装Web依赖
pip install fastapi uvicorn jinja2 aiofiles
```

### 2. 启动Web界面

```bash
# 方法1：使用启动脚本
python run_web_interface.py

# 方法2：直接启动FastAPI服务器
uvicorn data_service.web.api_server:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 访问界面

打开浏览器访问：http://localhost:8000

## 🎯 功能特性

### 📊 仪表板 (Dashboard)
- **系统状态监控** - 实时显示系统运行状态
- **性能指标** - 总收益、夏普比率、最大回撤等
- **风险指标** - VaR、CVaR、Beta等风险指标
- **权益曲线** - 交互式收益曲线图表
- **投资组合分配** - 饼图显示资产配置
- **最近活动** - 实时活动日志
- **最近交易** - 交易记录表格

### 🎮 策略管理 (Strategy Management)
- **策略列表** - 显示所有可用策略
- **策略详情** - 查看策略配置和性能
- **创建策略** - 通过表单创建新策略
- **启动/停止** - 控制策略运行状态
- **策略回测** - 运行策略回测并查看结果

### 📈 回测系统 (Backtest)
- **回测配置** - 设置回测参数
- **策略选择** - 选择要回测的策略
- **时间范围** - 设置回测时间范围
- **结果展示** - 显示回测结果和图表

### 💼 投资组合管理 (Portfolio)
- **持仓信息** - 显示当前持仓
- **投资组合摘要** - 总价值、现金、已投资金额
- **盈亏分析** - 每日和总盈亏
- **权重分配** - 各资产权重

### 🤖 AI分析 (AI Analysis)
- **情感分析** - 分析文本情感
- **市场分析** - AI驱动的市场分析
- **实时结果** - 即时显示分析结果

## 🔧 API接口

### 系统状态
```http
GET /api/system/status
```

### 策略管理
```http
GET /api/strategies
POST /api/strategies
PUT /api/strategies/{id}
DELETE /api/strategies/{id}
POST /api/strategies/{id}/start
POST /api/strategies/{id}/stop
```

### 回测
```http
POST /api/backtest/run
```

### AI分析
```http
POST /api/ai/analyze
```

### 市场数据
```http
GET /api/market/data/{symbol}
```

### 投资组合
```http
GET /api/portfolio/status
```

### 交易记录
```http
GET /api/trades/recent
```

## 🎨 界面截图

### 主仪表板
- 系统状态概览
- 性能指标卡片
- 实时图表
- 活动日志

### 策略管理
- 策略卡片网格
- 策略详情模态框
- 启动/停止控制

### 回测界面
- 配置表单
- 结果展示
- 性能图表

## 🔒 安全特性

- **CORS支持** - 跨域请求处理
- **输入验证** - Pydantic数据验证
- **错误处理** - 统一的错误响应
- **日志记录** - 完整的操作日志

## 📱 响应式设计

- **移动端适配** - 支持手机和平板
- **桌面端优化** - 大屏幕显示优化
- **触摸友好** - 支持触摸操作

## 🚀 部署

### 开发环境
```bash
python run_web_interface.py
```

### 生产环境
```bash
# 使用Gunicorn
gunicorn data_service.web.api_server:app -w 4 -k uvicorn.workers.UvicornWorker

# 使用Docker
docker build -t trading-system .
docker run -p 8000:8000 trading-system
```

### 反向代理 (Nginx)
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

## 🔧 配置

### 环境变量
```bash
export TRADING_SYSTEM_HOST=0.0.0.0
export TRADING_SYSTEM_PORT=8000
export TRADING_SYSTEM_DEBUG=true
```

### 配置文件
创建 `config.json`:
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

## 🐛 故障排除

### 常见问题

1. **端口被占用**
   ```bash
   # 查看端口占用
   netstat -tulpn | grep 8000
   
   # 杀死进程
   kill -9 <PID>
   ```

2. **依赖缺失**
   ```bash
   pip install -r requirements.txt
   ```

3. **权限问题**
   ```bash
   # Linux/Mac
   chmod +x run_web_interface.py
   
   # Windows
   python run_web_interface.py
   ```

### 日志查看
```bash
# 查看应用日志
tail -f logs/trading_system.log

# 查看错误日志
tail -f logs/error.log
```

## 📈 性能优化

### 前端优化
- 图表懒加载
- 数据缓存
- 压缩静态资源

### 后端优化
- 数据库连接池
- Redis缓存
- 异步处理

## 🔮 未来计划

- [ ] 实时数据推送 (WebSocket)
- [ ] 用户认证和权限管理
- [ ] 多语言支持
- [ ] 移动端应用
- [ ] 高级图表功能
- [ ] 策略回测对比
- [ ] 风险管理面板
- [ ] 报告生成器

## 📞 支持

如有问题或建议，请：
1. 查看文档
2. 检查日志
3. 提交Issue
4. 联系开发团队

---

**Trading System Web Interface** - 让交易系统管理变得简单高效！ 🚀 