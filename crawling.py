import requests
from bs4 import BeautifulSoup
import re

title = [ ] # 영화 제목 리스트 : o
movie_rate = [ ] # 영화 등급 : o
netizen_rate = [ ] # 네티즌 평점 : o
netizen_count = [ ] # 네티즌 평점 참여자 수 : o
journalist_score = [ ] # 기자평론가 평점 : o
journalist_count = [ ] # 기자평론가 참여자수 : o
scope = [ ] # 개요 : o
playing_time = [ ] # 상영시간 :
opening_date = [ ] # 개봉날짜 :
director = [ ] # 감독 : o
image = [ ] # 영화 대표 이미지 주소 : o


url = 'https://movie.naver.com/movie/running/current.naver'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')






# 제목 추출
k=soup.select_one('#content > div.article > div:nth-child(1) ')
titles = k.select('li > dl > dt > a')
for i in titles:
    title.append(i.get_text())
print("제목 수 : ", len(title))
    






# 등급 추출 후 출력 값 변경해서 리스트에 넣기
a=soup.select_one('#content > div.article > div:nth-child(1) ')
scopes = a.select('li > dl > dt')

for i in scopes:
    s = i.select_one('span')
    movie_rate.append(i.get_text())

for i in range(0,len(scope)):
    if movie_rate[i][2]=='5':
        movie_rate[i]="15세 관람가"
    elif movie_rate[i][2]=='2':
        movie_rate[i]='12세 관람가'
    elif movie_rate[i][2]=='소':
        movie_rate[i]='청소년 관람 불가'
    elif movie_rate[i][2]=='체':
        movie_rate[i]='전체 관람가'
    else:
        movie_rate[i]='정보 없음'                
print("등급 수 : ",len(movie_rate))







# 네티즌 평점 


net=soup.select_one('#content > div.article > div:nth-child(1) ')
net=net.select('li > dl > dd.star > dl > dd:nth-child(2) > div > a >span.num')

for i in net:
    netizen_rate.append(float(i.get_text()))

print("네트즌 평점 수 : ", len(netizen_rate))







# 네티즌 평점 참여자 수 

netnum=soup.select_one('#content > div.article > div:nth-child(1)')
netnum=netnum.select('li > dl > dd.star > dl > dd:nth-child(2) > div > a > span.num2 > em')

for i in netnum:
    netizen_count.append(i.get_text())

print("네트즌 평점 참여자 수 : ", len(netizen_count))







# 기자 평론가 평점
jr = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul')
jr = jr.select('li > dl > dd.star > dl ' )


for i in jr:
    s = i.select_one('dd:nth-child(4) > div > a > span.num')
    if s is None:
        journalist_score.append("정보 없음")
    else:
        journalist_score.append(float(s.get_text()))
print("기자 평론가 평점 수 : ",len(journalist_score))    








# 기자 평론가 참여자 수 
jrnum = soup.select_one("#content > div.article > div:nth-child(1) > div.lst_wrap > ul ")
jrnum = jrnum.select('li > dl > dd.star > dl')
for i in jrnum:
    s = i.select_one('dd:nth-child(4) > div > a > span.num2 > em')
    if s is None:
        journalist_count.append("정보 없음")
    else:
        journalist_count.append(s.get_text())   
 
print("기자 평론가 참여자 수 : ",len(journalist_count))






# 개요 
geyo = soup.select_one("#content > div.article > div:nth-child(1) > div.lst_wrap > ul")
geyo = geyo.select('li > dl > dd:nth-child(3) > dl > dd:nth-child(2) > span.link_txt ')

strs = ''
for i in geyo:
    k = i.find_all('a')
    for j in k:
        strs += str( j.get_text()+" " )
    scope.append(strs)    
print('개요 수 : ', len(scope))  




# 상영 시간 : 진행 중

ten = {'0','1','2','3','4','5','6','7','8','9'}

time = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul ')
time = list(time.get_text())

for i in range(0,len(time)):
    if time[i]=="분":
        if time[i-3] in ten:
            playing_time.append("".join((time[i-3:i+1])))
        else:
            playing_time.append("".join((time[i-2:i+1])))    

print("상영 시간의 수 : ", len(playing_time))

# 감독 
dir = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul')
dir = dir.select('li > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span ')
st = ""
for i in dir:
    k = i.find_all('a')
    for j in k:
        st += str( j.get_text()+" " )
    director.append(st)    

print("감독 수 : ",(len(director)))


# 영화 대표 이미지 주소 
img = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul ')
img = img.select('li > div > a')
for i in img:
    q = (i.img)
    k = q.get('src')
    image.append(k)

print("영화 이미지 수 : ",len(image))
