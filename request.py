import requests
import json

cotaçao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotaçao = cotaçao.json()

dolar = cotaçao['USDBRL']['bid']
euro = cotaçao['EURBRL']['bid']
btc = cotaçao['BTCBRL']['bid']