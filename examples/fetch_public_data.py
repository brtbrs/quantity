from data_service.fetchers import BinanceFetcher
import pandas as pd

pd.set_option('display.max_rows', 10)


def main():
    # 初始化 fetcher (不需要 API key)
    fetcher = BinanceFetcher()

    try:
        symbol = "BTCUSDT"

        # 获取历史K线数据
        df = fetcher.fetch_historical_data(
            symbol=symbol,
            interval="1h",  # 1小时K线
            limit=1,
        )
        latest_close = float(df["close"].iloc[-1])
        print(f"\n{symbol} 最新收盘价(1h): ${latest_close:,.2f}")

        # 打印更多历史数据
        df = fetcher.fetch_historical_data(symbol=symbol, interval="1h", limit=200)
        print("\n历史数据最后5条:")
        print(df.tail())

        # 获取市场深度（订单簿）
        depth = fetcher.get_order_book(symbol, limit=5)
        print("\n市场深度:")
        print("买盘:", depth['bids'])
        print("卖盘:", depth['asks'])

    except Exception as e:
        print(f"错误: {str(e)}")


if __name__ == "__main__":
    main()
