# function.py
x = 1 
def func(a):
    return a + x 

#함수를 호출
retValue = func(1)
print(retValue)
#함수를 정의 
def func2(a):
    x = 2 
    return a + x 

#함수를 호출
retValue = func2(1)
print(retValue)

#객체를 매개변수(인자)로 받는 경우 
#복사본을 생성해서 사용 변경
def change(x):
    #복사본을 별도로 생성 
    x = x[:]
    x[0] = 'H'
    print("함수내부:",  x)

wordlist = ['J','A','M']
change(wordlist)
print("함수 호출후:", wordlist)

#전역변수를 초기화
g = 1 
def testScope(a):
    global g 
    g = 2 
    return g + a 

#함수를 호출
print(testScope(1))
print("전역변수 g:", g)

#기본값이 있는 함수 정의
def Times(a=10, b=20):
    return a * b

#함수 호출
print(Times())
print(Times(5))
print(Times(5,6))

#URL을 생성하는 함수
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#함수 호출
print(connectURI("credu.com", "8080"))
print(connectURI(port="80", server="test.com"))



