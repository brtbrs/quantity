import logging

logger = logging.getLogger(__name__)

# Import fetchers with error handling
try:
    from .binance_fetcher import BinanceFetcher
except ImportError as e:
    logger.warning(f"BinanceFetcher import failed: {e}")
    BinanceFetcher = None

try:
    from .alpha_vantage_fetcher import AlphaVantageFetcher
except ImportError as e:
    logger.warning(f"AlphaVantageFetcher import failed: {e}")
    AlphaVantageFetcher = None

try:
    from .yahoo_fetcher import YahooFetcher
except ImportError as e:
    logger.warning(f"YahooFetcher import failed: {e}")
    YahooFetcher = None

__all__ = ['BinanceFetcher', 'AlphaVantageFetcher', 'YahooFetcher']
