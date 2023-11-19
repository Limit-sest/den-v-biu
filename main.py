import requests
from datetime import datetime
from time import sleep
from pytz import timezone
from instagrapi import Client
import json

response = requests.get("https://svatkyapi.cz/api/day").json()
svatek = response["name"]
day_number = response["dayNumber"]
day_week = response["dayInWeek"]
month = response["month"]["genitive"]

username = ""
password = ""

cl = Client()
cl.login(username,password)

def check_time():
    time = datetime.now(timezone('Europe/Prague'))
    if time.hour == 0:
        return True
    else:
        return False

def update_bio(line1,line2):
    try:
        cl.account_edit(biography=line1+"\n"+line2)
        print(f"Updated bio successfully to:\n{line1}\n{line2}")
    except Exception as e: print(e)

while True:
    if check_time():
        line1 = "📅 Dnes je "+day_week+", "+day_number+". "+month
        line2 = "🎀 Svátek má "+svatek
        update_bio(line1,line2)
    sleep(3600)#1 hour


