# coding: utf8

import xml.etree.ElementTree as XML_ETREE
import path_util
import xtrader
import xtrader.api as xtrader_api
import ccxt

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
    biance_cfg = xtrader_api.load_biance_cfg(cfg_dir)
    # okx交易接口
    #exchange = xtrader_api.build_okx_exchange(proxy_cfg, okx_cfg)
    # biance交易接口
    exchange = xtrader_api.build_biance_exchange(proxy_cfg, biance_cfg)
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
    #LOG_INFO("%s", result)
    LOG_INFO("SHIB现货持仓信息: %s", result["SHIB"])
    # 获取未订单
    LOG_INFO("获取未成交订单信息")
    result = exchange.fetch_open_orders("DOGE/USDT")
    LOG_INFO("%s", result)
    # 获取关闭交订单
    LOG_INFO("获取已成交订单")
    result = exchange.fetch_closed_orders(BTC_USDT_SYMBOL)
    LOG_INFO("%s", result)
    # 获取合约持仓
    LOG_INFO("获取合约持仓(注意合约交易对字符串有区别)")
    result = exchange.fetch_open_interest("1000SHIB/USDT:USDT")
    LOG_INFO("%s", result)
    # 合约交易历史 fetchOpenInterestHistory
    LOG_INFO("获取合约交易历史记录")
    result = exchange.fetch_open_interest_history("1000SHIB/USDT:USDT")
    LOG_INFO("%s", result)
    LOG_INFO("合约持仓模式查询")
    #result = exchange.fetch_account_positions(["1000SHIB/USDT:USDT"])
    result = exchange.fetch_position_mode(symbol = "1000SHIB/USDT:USDT", params = {
        "subType" : "linear"
    })
    LOG_INFO("%s", result)  # 确认允许双向持有仓位
    # 合约下单操作
    if create_order(exchange):
        LOG_INFO("下单成功")
    else:
        LOG_INFO("下单失败")

def create_order(exchange: ccxt.Exchange):
    ''''''
    LOG_INFO("合约下单测试")
    create_success = False
    try:
        # 无法使用 exchange.set_sandbox_mode(True)   # 调试模式
        '''
        positionSide:
            BOTH:
            LONG: 多
            SHORT: 空
        side:
            buy:  买
            sell: 卖

        buy + long  开多
        buy + short 平空
        sell + short 开空
        sell + long  平多
        '''
        exchange.options['defaultType'] = "future"  # 默认合约模式 future spot
        order = exchange.create_order(
            symbol="1000SHIB/USDT:USDT",  # 币种  注意合约模式不一样
            type="limit",  # 限价单 limit  market
            side="sell",  # 交易方向  buy(多) sell(空)
            amount=5,  # 交易数量
            price=1.1,    # 价格
            params={
                "timeInForce": "GTC",  # 一直有效直到手动取消
                "positionSide": "both", # BOTH LONG SHORT
                "hedged": True,
                #'dualSidePosition': True, 无效
            }
        )
        LOG_INFO("create order resturn: %s", order)
        create_order = True
    except ccxt.NetworkError as e:
        LOG_INFO("网络错误：%s", e)
    except ccxt.ExchangeError as e:
        LOG_INFO("交易所错误：%s", e)
    except ValueError as e:
        LOG_INFO("参数值错误：%s", e)
    except Exception as e:
        LOG_INFO("其他未知错误：%s", e)
        import traceback
        LOG_ERROR("%s", traceback.format_exc())
    return create_success

if __name__ == "__main__":
    main()