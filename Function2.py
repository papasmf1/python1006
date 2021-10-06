# Function2.py 
#가변형식의 경우(파이썬은 Pass By Reference)
def change(x):
    #내부에서 복사본을 만들기
    #리스트에서 [:]은 복사본을 만들어 달라는 의미 
    #x1은 복사된 지역변수
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)


#global키워드 사용 
#전역변수로 초기화
g = 1 
def testScope(a):
    #불변형식인 전역변수를 읽기 + 쓰기 가능 
    global g 
    g = 2 
    return a+g 

#함수 호출
print( testScope(1) )
print("전역변수 g:", g)


#기본값을 사용
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자 방식(파라메터명 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자(내부에서 튜플로 받아서 처리)
def union(*ar):
    #지역변수를 리스트로 초기화 
    result = []
    #HAM(0)  | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #아직 result에 포함되지 않았으면 
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )