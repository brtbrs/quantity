from binance.client import Client
from datetime import datetime
import pandas as pd
import logging
from typing import Optional, Dict, Callable
import os
from ..utils.exceptions import DataFetchError


class BinanceFetcher:
    """Binance数据获取器"""

    def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None, tld: Optional[str] = None):
        """
        初始化Binance客户端
        :param api_key: Binance API key (可选)
        :param api_secret: Binance API secret (可选)
        :param tld: Binance API top-level domain, defaults to BINANCE_TLD env or 'com'
        """
        self.logger = logging.getLogger(__name__)
        self.api_key = api_key
        self.api_secret = api_secret
        self.tld = tld or os.getenv("BINANCE_TLD", "com")
        self.client = None
        self.bm = None  # WebSocket管理器
        self.ws_connections = {}  # 存储WebSocket连接
        self.logger.info(f"Binance fetcher initialized (lazy client mode, tld={self.tld})")

    def _get_client(self) -> Client:
        """Lazily create Binance client to avoid network failures during service startup."""
        if self.client is not None:
            return self.client

        try:
            self.client = Client(self.api_key, self.api_secret, tld=self.tld, ping=False)
        except TypeError:
            # Fallback for python-binance versions without `ping` argument
            self.client = Client(self.api_key, self.api_secret, tld=self.tld)

        return self.client

    def fetch_historical_data(
        self,
        symbol: str = "BTCUSDT",
        interval: str = "1h",
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limit: int = 1000
    ) -> pd.DataFrame:
        try:
            start_str = int(start_time.timestamp() * 1000) if start_time else None
            end_str = int(end_time.timestamp() * 1000) if end_time else None

            client = self._get_client()
            klines = client.get_klines(
                symbol=symbol,
                interval=interval,
                startTime=start_str,
                endTime=end_str,
                limit=limit
            )

            df = pd.DataFrame(klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_volume', 'trades', 'taker_buy_base',
                'taker_buy_quote', 'ignore'
            ])

            numeric_columns = ['open', 'high', 'low', 'close', 'volume']
            df[numeric_columns] = df[numeric_columns].astype(float)
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)

            self.logger.info(f"Successfully fetched {len(df)} records for {symbol}")
            return df

        except Exception as e:
            self.logger.error(f"Error fetching historical data: {str(e)}")
            raise DataFetchError(f"Failed to fetch historical data: {str(e)}")

    async def start_websocket(self, symbol: str, callback: Callable[[Dict], None]):
        try:
            if not self.bm:
                from binance.websockets import BinanceSocketManager
                self.bm = BinanceSocketManager(self._get_client())

            conn_key = f"{symbol.lower()}@kline_1m"

            def handle_socket_message(msg):
                try:
                    if msg['e'] == 'kline':
                        data = {
                            'symbol': msg['s'],
                            'timestamp': pd.to_datetime(msg['E'], unit='ms'),
                            'open': float(msg['k']['o']),
                            'high': float(msg['k']['h']),
                            'low': float(msg['k']['l']),
                            'close': float(msg['k']['c']),
                            'volume': float(msg['k']['v'])
                        }
                        callback(data)
                except Exception as e:
                    self.logger.error(f"Error processing websocket message: {str(e)}")

            self.ws_connections[conn_key] = self.bm.start_kline_socket(
                symbol=symbol,
                callback=handle_socket_message,
                interval='1m'
            )

            self.bm.start()
            self.logger.info(f"WebSocket started for {symbol}")

        except Exception as e:
            self.logger.error(f"Error starting websocket: {str(e)}")
            raise

    def stop_websocket(self, symbol: str):
        try:
            conn_key = f"{symbol.lower()}@kline_1m"
            if conn_key in self.ws_connections:
                self.bm.stop_socket(self.ws_connections[conn_key])
                del self.ws_connections[conn_key]
                self.logger.info(f"WebSocket stopped for {symbol}")
        except Exception as e:
            self.logger.error(f"Error stopping websocket: {str(e)}")
            raise

    def get_order_book(self, symbol: str = "BTCUSDT", limit: int = 100) -> Dict:
        try:
            client = self._get_client()
            depth = client.get_order_book(symbol=symbol, limit=limit)
            return {
                'bids': [[float(price), float(qty)] for price, qty in depth['bids']],
                'asks': [[float(price), float(qty)] for price, qty in depth['asks']]
            }
        except Exception as e:
            self.logger.error(f"Error fetching order book: {str(e)}")
            raise DataFetchError(f"Failed to fetch order book: {str(e)}")

    def get_market_depth(self, symbol: str = "BTCUSDT", limit: int = 100) -> Dict:
        """Backward-compatible alias for order book."""
        return self.get_order_book(symbol=symbol, limit=limit)

    def get_recent_trades(self, symbol: str = "BTCUSDT", limit: int = 100) -> pd.DataFrame:
        try:
            client = self._get_client()
            trades = client.get_recent_trades(symbol=symbol, limit=limit)
            df = pd.DataFrame(trades)
            df['time'] = pd.to_datetime(df['time'], unit='ms')
            df['price'] = df['price'].astype(float)
            df['qty'] = df['qty'].astype(float)
            return df
        except Exception as e:
            self.logger.error(f"Error fetching recent trades: {str(e)}")
            raise DataFetchError(f"Failed to fetch recent trades: {str(e)}")
