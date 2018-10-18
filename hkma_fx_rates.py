import pprint
import requests

DATE = '2018-09-01'
HKMA_API = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily'


def main():
    params = {'from': DATE, 'to': DATE, 'choose': 'end_of_day'}
    r = requests.get(url=HKMA_API, params=params)
    if r.status_code == 200:
        r = r.json()
        if r.get('header').get('success'):
            results = r.get('result').get('records')[0]
            pprint.pprint(results)
        else:
            print('Something went wrong!')
            print(r.get('header').get('err_msg'))
    else:
        r.raise_for_status()


if __name__ == '__main__':
    main()
