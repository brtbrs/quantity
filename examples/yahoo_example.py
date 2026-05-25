from data_service.fetchers.yahoo_fetcher import YahooFetcher
import pandas as pd


def main():
    symbol = "AAPL"
    fetcher = YahooFetcher()

    print(f"获取 {symbol} 历史数据...")
    history = fetcher.fetch_historical_data(symbol=symbol, interval="1d")

    if history.empty:
        print("未获取到历史数据")
        return

    print("\n最近5条历史数据:")
    print(history.tail())

    print(f"\n获取 {symbol} 公司信息...")
    info = fetcher.get_company_info(symbol)
    print(info)


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    main()
