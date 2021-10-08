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
f = open("c:\\work\\clien.txt", "wt", encoding="utf-8")
for n in range(0,10):
        time.sleep(2)
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #일반 커뮤니트는 디코딩을 해야 한다. 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # <span class="subject_fixed" data-role="list-title-text">
	# 	아이폰XR 64Gb 화이트 팝니다(가격수정)
	# </span>
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        title = item.text  
                        if (re.search('아이폰', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                except:
                        pass
        
print("웹크롤링 종료")
f.close() 

