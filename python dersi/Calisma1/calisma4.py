import requests
from bs4 import BeautifulSoup
url ="https://www.includekarabuk.com/kbudersnotlari.php"

response =requests.get(url) #Wep sitemizi cekiyoruz

htmlIcerigi = response.content #Wep sayfamizin icerigini aliyoruz

#Wep sitemizi parcalamak icin BEatifulSoup objesine atiyoruz
soup = BeautifulSoup(htmlIcerigi, "html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


#print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.

#print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.
"""for i in soup.find_all("a"):
    print(i.get("href"))
"""
"""for i in soup.find_all("a"):
    print(i.text)
"""

print(response)
for i in soup.find_all("div" , {"id" : "outerFrame"}):
    print(i.text)