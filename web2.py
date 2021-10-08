# web2.py 
#웹서버와 통신할 때 
import urllib.request
#크롤링에 사용 
from bs4 import BeautifulSoup

#네이버 웹서버에 부탁 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색을 스프 객체 생성 
soup = BeautifulSoup(data, "html.parser")

#다중 라인 주석: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail?titleId">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")

print("갯수:{0}".format( len(cartoons) ))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print( title )
print( link )
