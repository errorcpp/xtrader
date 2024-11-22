# coding: utf8

import xml.etree
import xml.etree.ElementTree as XML_ETREE
import ccxt
import xmltodict
import os
import path_util

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

def build_okx_exchange(proxy_cfg, okx_cfg):
    '''
    @biref 构造okx交易所对象
    '''
    okx_exchange = ccxt.okx()
    #okx_exchange.http_proxy = proxy_cfg.get("proxy_cfg", {}).get("http_proxy", "http://127.0.0.1:7890")
    okx_exchange.https_proxy = proxy_cfg.get("proxy_cfg", {}).get("https_proxy", "http://127.0.0.1:7890")
    return okx_exchange