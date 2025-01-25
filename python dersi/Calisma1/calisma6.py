import requests
from bs4 import BeautifulSoup

siteAdresi = "https://www.includekarabuk.com/kbudersnotlari.php"

cekilenVeri = requests.get(siteAdresi)

htmlIcerigi = cekilenVeri.content

soup = BeautifulSoup(htmlIcerigi,"html.parser")

veri = soup.find_all("div",{"id" : "content"},"tr")


for i in veri:
    print(i.text)


