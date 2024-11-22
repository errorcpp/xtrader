# coding: utf8

import xml.etree.ElementTree as XML_ETREE
import path_util
import xtrader
import xtrader.api as xtrader_api

# 目标交易对列表
TARGET_SYMBOLS = ["BTC/USDT", "SHIB/USDT"]
# 单独的交易对
BTC_USDT_SYMBOL = "BTC/USDT"
SHIB_USDT_SYMBOL = "SHIB/USDT"


def main():
    ''''''
    LOG_DEBUG("enter main")
    cfg_dir = path_util.get_abs_dir_from_file_path(__file__)
    proxy_cfg = xtrader_api.load_proxy_cfg(cfg_dir)
    okx_cfg = xtrader_api.load_okx_cfg(cfg_dir)
    exchange = xtrader_api.build_okx_exchange(proxy_cfg, okx_cfg)
    #print(exchange.load_markets())
    # 实时行情获取
    LOG_INFO("获取[%s]的实时价格信息", TARGET_SYMBOLS)
    result = exchange.fetch_tickers(TARGET_SYMBOLS)
    LOG_INFO("%s", result)
    # 柱线图-分钟级别
    LOG_INFO("获取[%s]的分钟级别柱状图", BTC_USDT_SYMBOL)
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1m", limit=100)
    LOG_INFO("%s", result)
    # 柱线图-小时级别
    LOG_INFO("获取[%s]的小时级别柱状图", BTC_USDT_SYMBOL)
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1h")
    LOG_INFO("%s", result)
    # 柱线图-天级别, limit参数控制需要获取多少个柱子
    LOG_INFO("获取[%s]的天级别柱状图", BTC_USDT_SYMBOL)
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1d", limit=1)
    LOG_INFO("%s", result)
    # 获取仓位信息
    LOG_INFO("获取仓位信息")
    result = exchange.fetch_balance()
    LOG_INFO("%s", result)
    # 获取未订单
    LOG_INFO("获取未成交订单信息")
    result = exchange.fetch_open_orders(BTC_USDT_SYMBOL)
    LOG_INFO("%s", result)
    # 获取关闭交订单
    LOG_INFO("获取已成交订单")
    result = exchange.fetch_closed_orders(BTC_USDT_SYMBOL)
    LOG_INFO("%s", result)
    # 获取合约持仓
    LOG_INFO("获取合约持仓(注意合约交易对字符串有区别)")
    result = exchange.fetch_open_interest("BTC/USDT:USDT")
    LOG_INFO("%s", result)
    # 合约交易历史 fetchOpenInterestHistory

if __name__ == "__main__":
    main()