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

    #content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(28) > dl > dt > a




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

# 네티즌 평점 - 순서 오류

#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(29) > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(30) > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num
net=soup.select_one('#content > div.article > div:nth-child(1) ')
net=net.select('li > dl > dd.star > dl > dd:nth-child(2) > div > a >span.num')

for i in net:
    netizen_rate.append(float(i.get_text()))




# 네티즌 평점 참여자 수 - 순서 오류

netnum=soup.select_one('#content > div.article > div:nth-child(1)')
netnum=netnum.select('li > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num2 > em')

for i in netnum:
    netizen_count.append(i.get_text())




# 기자 평론가 평점 - 순서 오류
jr = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul')
jr = jr.select('li > dl > dd.star > dl ' )


for i in jr:
    s = i.select_one('dd:nth-child(4) > div > a > span.num')
    if s is None:
        journalist_score.append("정보 없음")
    else:
        journalist_score.append(float(s.get_text()))
    

#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd.star > dl > dd:nth-child(4) > div > a > span.num
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(2) > dl > dd.star > dl > dd:nth-child(4) > div > a > span.num



# 기자 평론가 참여자 수 
jrnum = soup.select_one("#content > div.article > div:nth-child(1) > div.lst_wrap > ul ")
jrnum = jrnum.select('li > dl > dd.star > dl')
for i in jrnum:
    s = i.select_one('dd:nth-child(4) > div > a > span.num2 > em')
    if s is None:
        journalist_count.append("정보 없음")
    else:
        journalist_count.append(s.get_text())   
print(journalist_count)         



#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd.star > dl > dd:nth-child(4) > div > a > span.num2 > em
#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(2) > dl > dd.star > dl > dd:nth-child(4) > div > a > span.num2 > em