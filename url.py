from bs4 import BeautifulSoup
import requests

response = requests.get("https://finance.i.ua/converter/")
if response.status_code==200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup1 = soup.find_all(class_="value -decrease")
    grn = soup1[0].find("span")
    grn1=grn.text
grn2 = int(input("Input UAH:"))
doll = grn2 / float(grn1)
print(doll)