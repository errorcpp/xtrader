# okx-api接口说明

## fetch_tickers: 获取实时行情信息
* 输入：交易对数组例如 ```["BTC/USDT", "SHIB/USDT"]```
* 输出：交易对和行情信息的一个字典对象，格式如下
``` json
{
    'BTC/USDT':
    {
        'symbol': 'BTC/USDT',
        'timestamp': 1731575722410,
        'datetime': '2024-11-14T09:15:22.410Z',
        'high': 93263.0,
        'low': 87120.0,
        'bid': 90683.3,
        'bidVolume': 0.01223691,
        'ask': 90683.4,
        'askVolume': 1.63224981,
        'vwap': 90508.10304419548,
        'open': 87447.3,
        'close': 90683.4,
        'last': 90683.4,
        'previousClose': None,
        'change': 3236.1,
        'percentage': 3.700628835881725,
        'average': 89065.3,
        'baseVolume': 22313.62189148,
        'quoteVolume': 2019563589.4432878,
        'markPrice': None,
        'indexPrice': None,
        'info':
        {
            'instType': 'SPOT',
            'instId': 'BTC-USDT',
            'last': '90683.4',
            'lastSz': '0.00011897',
            'askPx': '90683.4',
            'askSz': '1.63224981',
            'bidPx': '90683.3',
            'bidSz': '0.01223691',
            'open24h': '87447.3',
            'high24h': '93263',
            'low24h': '87120',
            'volCcy24h': '2019563589.443287824',
            'vol24h': '22313.62189148',
            'ts': '1731575722410',
            'sodUtc0': '90378.4',
            'sodUtc8': '92525.7'
        }
    },
    'SHIB/USDT':
    {
        'symbol': 'SHIB/USDT',
        'timestamp': 1731575722311, 'datetime': '2024-11-14T09:15:22.311Z', 'high': 2.7939e-05, 'low': 2.3525e-05, 'bid': 2.608e-05, 'bidVolume': 410534.0, 'ask': 2.6083e-05, 'askVolume': 11728858.0, 'vwap': 2.5921887095885e-05, 'open': 2.4009e-05, 'close': 2.608e-05, 'last': 2.608e-05, 'previousClose': None, 'change': 2.071e-06, 'percentage': 8.625931942188346, 'average': 2.5044e-05, 'baseVolume': 6043353327507.0, 'quoteVolume': 156655122.63618043, 'markPrice': None, 'indexPrice': None, 'info': {'instType': 'SPOT', 'instId': 'SHIB-USDT', 'last': '0.00002608', 'lastSz': '196684', 'askPx': '0.000026083', 'askSz': '11728858', 'bidPx': '0.00002608', 'bidSz': '410534', 'open24h': '0.000024009', 'high24h': '0.000027939', 'low24h': '0.000023525', 'volCcy24h': '156655122.636180432', 'vol24h': '6043353327507', 'ts': '1731575722311', 'sodUtc0': '0.000025822', 'sodUtc8': '0.000026888'}}
}
```