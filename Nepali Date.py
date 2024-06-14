import requests
from plyer import notification

date = requests.get('https://nepali-datetime.amitgaru.me/date?format=%d-%B-%y')

data = date.json()

notification.notify(
    title='Nepali Date',
    message=data['data'], 
)