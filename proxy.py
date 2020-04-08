# CODE BY AKASAKAID
# CUMA SCRAPING WEB BIASA TYDACK ADA YANG ISTIMEWA
import requests,os
from bs4 import BeautifulSoup as bs
r = requests.Session()
url = 'https://free-proxy-list.net/'
def bn():
	if os.name == 'nt':os.system('cls')
	else:os.system('clear')
	print("""
	PROXY GRABBER
	POWERED BY HTTPS://FREE-PROXY-LIST.NET
	CODE BY AKASAKAID
	""")
bn()
input("TEKAN ENTER UNTUK MEMULAI...")
bn()
a = r.get(url).text
b = bs(a,'html.parser')
c = b.find("tbody").findAll("tr")
for pr in c:
	ls = pr.findAll("td")
	print("proxy :",ls[0].text+":"+ls[1].text)
	print("https :",ls[6].text)
	print("lokasi:",ls[2].text)
	print(" ")
