# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식 
import re 
#대기시간 
import time 

#우리 웹사이트는 웹봇을 금지 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장
f = open("c:\\work\\todayhumor.txt", "wt", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머: 베스트게시판 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #일반 커뮤니트는 디코딩을 해야 한다. 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # <td class="subject">
        #    <a href="/board/view.php?"">
        #     오징어게임 전세계적인기 체감하기
        #    </a>
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.find("a").text 
                        if (re.search('오징어게임', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                except:
                        pass
        
print("웹크롤링 종료")
f.close() 

