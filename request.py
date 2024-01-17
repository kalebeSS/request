import requests

Url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

try:
    response = requests.get(Url)
    data = response.text
    if response.status_code ==200:
        print(data)
    else:
        print('não foi possivel consumir a api do site')

except Exception as ex:
    print(f'ocorreu um erro {ex}')
