# web1.py 
from bs4 import BeautifulSoup

#페이지를 로딩하기
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#문서의 <p>태그 전부 검색
#print( soup.find_all("p") )

#<p>태그 하나만 검색
#print( soup.find("p") )

#<p class='outer-text'>컨텐츠</p>: 필터링(걸러내기)
#print( soup.find_all("p", class_="outer-text") )

#<p id="first">
#print( soup.find_all(id="first") )

#태그의 컨텐츠만 출력하기 
for tag in soup.find_all("p"):
    #<p>컨텐츠</p>: 알맹이만 빼내기 ==> .text 
    content = tag.text 
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    print( content.strip() )

    




