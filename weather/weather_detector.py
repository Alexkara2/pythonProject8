import sqlite3
import datetime
from bs4 import BeautifulSoup
import requests
connection = sqlite3.connect("weather.sl3", 5)
cursor = connection.cursor()
time1 = str(datetime.datetime.now())

request = requests.get("https://pogoda.unian.net/85486-kiev")
if request.status_code==200:
    weat=BeautifulSoup(request.text, "html.parser")
    weat_list = weat.find_all(class_="info-now__c")
    weat_data = weat_list[0].find("div")
    weat_data1=weat_data.text


#cursor.execute("CREATE TABLE time (name TEXT);")
#cursor.execute("CREATE TABLE temperature (name TEXT);")
cursor.execute("INSERT INTO time (name) VALUES (time1);")
cursor.execute("INSERT INTO temperature (name) VALUES (weat_data1);")

connection.close()