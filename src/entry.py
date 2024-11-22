# coding: utf8

import xml.etree
import xml.etree.ElementTree as XML_ETREE
import ccxt
import xmltodict
import os
import path_util

# 目标交易对列表
TARGET_SYMBOLS = ["BTC/USDT", "SHIB/USDT"]
# 单独的交易对
BTC_USDT_SYMBOL = "BTC/USDT"
SHIB_USDT_SYMBOL = "SHIB/USDT"



# def load_proxy_cfg():
#     '''
#     @breif 加载代理配置
#     '''
#     path = path_util.get_abs_dir_from_file_path(__file__)
#     cfg_file_path = f"{path}/../.private/proxy.xml"
#     file = open(cfg_file_path, "r")
#     if not file:
#         raise f"open file faild, file_name={cfg_file_path}"
#     data = file.read()
#     proxy_cfg = xmltodict.parse(data)
#     #print(proxy_cfg)
#     return proxy_cfg

# def load_okx_cfg():
#     '''
#     @brief 加载okx交易所配置
#     '''
#     path = path_util.get_abs_dir_from_file_path(__file__)
#     cfg_file_path = f"{path}/../.private/okx.xml"
#     file = open(cfg_file_path, "r")
#     if not file:
#         raise f"open file faild, file_name={cfg_file_path}"
#     data = file.read()
#     okx_cfg = xmltodict.parse(data)
#     #print(okx_cfg)
#     return okx_cfg

# def build_okx_exchange(proxy_cfg, okx_cfg):
#     '''
#     @biref 构造okx交易所对象
#     '''
#     okx_exchange = ccxt.okx()
#     #okx_exchange.http_proxy = proxy_cfg.get("proxy_cfg", {}).get("http_proxy", "http://127.0.0.1:7890")
#     okx_exchange.https_proxy = proxy_cfg.get("proxy_cfg", {}).get("https_proxy", "http://127.0.0.1:7890")
#     return okx_exchange


def main():
    ''''''
    cfg_dir = path_util.get_abs_dir_from_file_path(__file__)
    proxy_cfg = load_proxy_cfg(cfg_dir)
    okx_cfg = load_okx_cfg(cfg_dir)
    exchange = build_okx_exchange(proxy_cfg, okx_cfg)
    #print(exchange.load_markets())
    # 实时行情获取
    result = exchange.fetch_tickers(TARGET_SYMBOLS)
    print(result)
    # 柱线图-分钟级别
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1m", limit=100)
    print(result)
    # 柱线图-小时级别
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1h")
    print(result)
    # 柱线图-天级别, limit参数控制需要获取多少个柱子
    result = exchange.fetch_ohlcv(BTC_USDT_SYMBOL, timeframe="1d", limit=1)
    print(result)

if __name__ == "__main__":
    main()