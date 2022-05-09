import requests
from bs4 import BeautifulSoup

title = [ ] # 영화 제목 리스트
movie_rate = [ ] # 영화 등급 
netizen_rate = [ ] # 네티즌 평점
netizen_count = [ ] # 네티즌 평점 참여자 수
journalist_score = [ ] # 기자평론가 평점
journalist_count = [ ] # 기자평론가 참여자수
scope = [ ] # 개요
playing_time = [ ] # 상영시간
opening_date = [ ] # 개봉날짜
director = [ ] # 감독
image = [ ] # 영화 대표 이미지 주소


url = 'https://movie.naver.com/movie/running/current.naver'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 제목 추출
k=soup.select_one('#content > div.article > div:nth-child(1) ')
titles = k.select('li > dl > dt > a')
for i in titles:
    title.append(i.get_text())


#content > div.article > div:nth-child(1)
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt

