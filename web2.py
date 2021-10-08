# web2.py 
#웹서버와 통신할 때 
import urllib.request
#크롤링에 사용 
from bs4 import BeautifulSoup

#페이징처리(1번에서 5번): URL주소를 동적으로 생성 
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #검색을 스프 객체 생성 
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")
    f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
    for item in cartoons:
        title = item.find("a").text 
        print( title.strip() )
        f.write(title.strip() + "\n")
    f.close() 

