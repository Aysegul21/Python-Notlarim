import requests
#wep sayfasındaki verileri ceker

from bs4 import BeautifulSoup
#verileri alıyoruz . mesela wep sayfası icinde sadece "c" harfi olanları almak

url = "https://www.npr.org/2023/02/07/1154913148/turkey-earthquake-fault-lines-syria"
response = requests.get(url)

html_icerigi = response.content #wep dokumanının html kismi (sayfa kayanagı kismi) karsimiza gelecek

soup = BeautifulSoup(html_icerigi,"html.parser")


print(soup.find_all("div",{"class":"yp-poi-box-2"}))






