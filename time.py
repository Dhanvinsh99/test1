#function that takes time using an api
import json
import requests
import os
import time
n = 0
while n == 0:
    response = requests.get('http://worldtimeapi.org/api/timezone/Indian/Cocos').text
    info= json.loads(response)
    ctime=str(info['datetime'])
    date=ctime[0:9]
    ttime=ctime[11:19]
    print('date:', date)
    print('time:', ttime)
    time.sleep(1)
    os.system('clear')
