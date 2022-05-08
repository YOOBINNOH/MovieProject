import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.naver'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title=soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a')
    print(title.getText())
    
else : 
    print(response.status_code)


