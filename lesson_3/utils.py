import requests

from datetime import datetime
from urllib import parse


def validate_bank(bank: str) -> str:
    bank_list_nb = ['nbu', 'NBU', 'NB', 'NationalBank', 'nationalbank', 'nb']
    bank_list_pb = ['pb', 'PB', 'NB', 'privatbank', 'PrivatBank']

    if bank in bank_list_nb:
        bank = 'NB'
    elif bank in bank_list_pb:
        bank = 'PB'
    else:
        return None

    return bank


def validate_rate_date(rate_date):
    """
    Валидация даты на правильность ввода
    :param list_date: список из отдельных кусков введенной даты
    :return: пересобранная дата в нужном отображении
    """

    if '.' in rate_date:
        list_date = rate_date.split('.')
    elif '-' in rate_date:
        list_date = rate_date.split('-')

    list_date = [int(num) for num in list_date]

    year = list_date.pop(list_date.index(max(list_date)))
    if year > datetime.now().year:
        rate_date = None

    list_date[0], list_date[1] = int(list_date[0]), int(list_date[1])

    if  0 < list_date[0] <= 12 and 12 < list_date[1] <= 31:
        day, month = list_date.pop(), list_date.pop()
    elif 0 < list_date[0] <= 31 and 0 < list_date[1] <= 12:
        month, day = list_date.pop(), list_date.pop()
    else:
        rate_date = None


    while rate_date is None:
        rate_date = input(f"{'-'*45}\nIncorrect date. Please try again: ")
        rate_date = validate_rate_date(rate_date)
        return rate_date

    day = '0' + str(day) if day < 10 else str(day)
    month = '0' + str(month) if month < 10 else str(month)
    year = str(year)

    rate_date = day + '.' + month + '.' + year

    return rate_date


def get_currency_iso_code(currency: str) -> int:
    '''
    Функція повертає ISO код валюти
    :param currency: назва валюти
    :return: код валюти
    '''
    currency_dict = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'AZN': 944,
        'CAD': 124,
        'PLN': 985,
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currencies information')


def get_currency_exchange_rate(currency_a: str,
                               currency_b: str) -> str:
    currency_code_a = get_currency_iso_code(currency_a)
    currency_code_b = get_currency_iso_code(currency_b)

    response = requests.get('https://api.monobank.ua/bank/currency')
    json = response.json()

    if response.status_code == 200:
        for i in range(len(json)):
            if json[i].get('currencyCodeA') == currency_code_a and json[i].get('currencyCodeB') == currency_code_b:
                date = datetime.fromtimestamp(
                    int(json[i].get('date'))
                ).strftime('%Y-%m-%d %H:%M:%S')
                rate_buy = json[i].get('rateBuy')
                rate_sell = json[i].get('rateSell')
                return f'exchange rate {currency_a} to {currency_b} for {date}: \n rate buy - {rate_buy} \n rate sell - {rate_sell}'
            return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"




#print(get_currency_exchange_rate('USD', 'UAH'))


def get_pb_exchange_rate(convert_currency: str,
                         bank: str,
                         rate_date: str) -> str:
    
    rate_date = validate_rate_date(rate_date)
    params = {
        'json': '',
        'date': rate_date,  # TODO додати функцію валідації формату дати
    }

    query = parse.urlencode(params)
    api_url = 'https://api.privatbank.ua/p24api/exchange_rates?'
    response = requests.get(api_url+query)
    json = response.json()
    bank = validate_bank(bank)
    

    if response.status_code == 200:
        rates = json['exchangeRate']
        for rate in rates:
            if rate['currency'] == convert_currency:
                if bank == 'NB':
                    try:
                        sale_rate = rate['saleRateNB']
                        purchase_rate = rate['purchaseRateNB']
                        return f'Exchange rate UAH to {convert_currency} for {rate_date} at {bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate NBU for {convert_currency}'
                    
                elif bank == 'PB':
                    try:
                        sale_rate = rate['saleRate']
                        purchase_rate = rate['purchaseRate']
                        return f'Exchange rate UAH to {convert_currency} for {rate_date} at {bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate PrivatBank for {convert_currency}'
                else:
                    return f'<h1><b>Rates for this bank is not supported! Only for PrivatBank and NationalBank!</b></h1>'
    else:
        try:
            return f'error {response.status_code}'
        except:
            return 'asdasdasd'


result = get_pb_exchange_rate('USD', 'PB', '2020.11.02')


print(result)
