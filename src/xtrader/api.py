# coding: utf8

import xml.etree.ElementTree as XML_ETREE
import ccxt
import xmltodict

def load_proxy_cfg(cfg_dir):
    '''
    @breif 加载代理配置
    '''
    path = cfg_dir #path_util.get_abs_dir_from_file_path(__file__)
    cfg_file_path = f"{path}/../.private/proxy.xml"
    file = open(cfg_file_path, "r")
    if not file:
        raise f"open file faild, file_name={cfg_file_path}"
    data = file.read()
    proxy_cfg = xmltodict.parse(data)
    #print(proxy_cfg)
    return proxy_cfg

def load_okx_cfg(cfg_dir):
    '''
    @brief 加载okx交易所配置
    '''
    path = cfg_dir #path_util.get_abs_dir_from_file_path(__file__)
    cfg_file_path = f"{path}/../.private/okx.xml"
    file = open(cfg_file_path, "r")
    if not file:
        raise f"open file faild, file_name={cfg_file_path}"
    data = file.read()
    okx_cfg = xmltodict.parse(data)
    #print(okx_cfg)
    return okx_cfg

def load_biance_cfg(cfg_dir):
    '''
    @breif 加载biance交易所配置
    '''
    path = cfg_dir #path_util.get_abs_dir_from_file_path(__file__)
    cfg_file_path = f"{path}/../.private/biance.xml"
    file = open(cfg_file_path, "r")
    if not file:
        raise f"open file faild, file_name={cfg_file_path}"
    data = file.read()
    okx_cfg = xmltodict.parse(data)
    #print(okx_cfg)
    return okx_cfg

def build_okx_exchange(proxy_cfg, okx_cfg):
    '''
    @biref 构造okx交易所对象
    '''
    okx_exchange = ccxt.okx()
    # 没有给代理配置，不设置代理
    if proxy_cfg:
        #okx_exchange.http_proxy = proxy_cfg.get("proxy_cfg", {}).get("http_proxy", "http://127.0.0.1:7890")
        okx_exchange.https_proxy = proxy_cfg.get("proxy_cfg", {}).get("https_proxy", "http://127.0.0.1:7890")
    okx_exchange.apiKey = okx_cfg["okx"]["api_cfg"]["api_key"]
    okx_exchange.secret = okx_cfg["okx"]["api_cfg"]["api_token"]
    okx_exchange.password = okx_cfg["okx"]["api_cfg"]["api_sec"]
    return okx_exchange

def build_biance_exchange(proxy_cfg, biance_cfg):
    '''
    @breif 构造biance交易所对象
    @param type string: 币安需要再初始化的时候明确交易类型是合约还是现货  future  spot
    '''
    exchange: ccxt.binance = ccxt.binance()
    if proxy_cfg:
        exchange.https_proxy = proxy_cfg.get("proxy_cfg", {}).get("https_proxy", "http://127.0.0.1:7890")
    exchange.apiKey = biance_cfg["biance"]["api_cfg"]["api_key"]
    exchange.secret = biance_cfg["biance"]["api_cfg"]["secret_key"]
    # , order_type = "spot" exchange.default
    return exchange