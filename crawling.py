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




# 등급 추출 후 출력 값 변경해서 리스트에 넣기
a=soup.select_one('#content > div.article > div:nth-child(1) ')
scopes = a.select('li > dl > dt')
for i in scopes:
    s = i.select_one('span')
    scope.append(i.get_text())

for i in range(0,len(scope)):
    if scope[i][2]=='5':
        scope[i]="15세 관람가"
    elif scope[i][2]=='2':
        scope[i]='12세 관람가'
    elif scope[i][2]=='소':
        scope[i]='청소년 관람 불가'
    elif scope[i][2]=='체':
        scope[i]='전체 관람가'
    else:
        scope[i]='정보 없음'                



# 네티즌 평점 추출
b=soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul ')
b=b.find_all(class_="num")

print(b[0])
print(b[1])
print(b[2])

#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(2) > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num