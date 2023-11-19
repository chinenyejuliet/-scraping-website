import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Elvi.html'
counts = int(input('Enter count:'))
position = int(input('Enter position:'))

for i in range(counts):
    html = urllib.request.urlopen(url).read()
    soup  = BeautifulSoup(html,'html.parser')
    
    tag = soup('a')
    url = tag[position - 1].get('href', None)
    print("Retrieving:",url)

lastname = url.split('_')[2].split(".")[0]
print(lastname)