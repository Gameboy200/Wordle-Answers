import requests
from datetime import datetime

try:
    def todayswordle():
        url = 'https://www.nytimes.com/svc/wordle/v2/'
        date = str(datetime.now().date())
        url += date + '.json'
        reponse = requests.get(url)
        data = reponse.json()
        answer = data['solution']
        return answer
except Exception as e:
    print(e)
    
try:
    def anywordle(date):
        year, month, day = map(int, date.split('-'))
        lowest = datetime(2021, 6, 19)
        check = datetime(year, month, day)
        check2 = check < lowest
        if check2:
            raise ValueError(f'{date} Is not a valid wordle date. Please use a date after 2021-6-19.')
        url = 'https://www.nytimes.com/svc/wordle/v2/'
        url += date + '.json'
        reponse = requests.get(url)
        data = reponse.json()
        answer = data['solution']
        return answer
except Exception as e:
    print(e)