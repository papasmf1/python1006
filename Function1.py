# Function1.py

#값을 반환하지 않는 함수
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

#함수 호출
retValue = setValue(5)
print( retValue )

#여러개의 값을 리턴(Tuple)
def swap(x,y):
    return y,x 

#호출
retValue = swap(10,20)
print( retValue )

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #함수 내부의 지역 변수
    retList = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출
#중단점(Break Point)
print( intersect("HAM", "SPAM") )

#내부를 좀 더 보기 
print( globals() )

#불변형식 연습
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )


#지역변수와 전역변수 충돌 (LGB)
#전역 변수 
x = 5 
def func1(y):
    return x+y 

#호출
print( func1(1) )

def func2(y):
    #지역 변수(Local Variable)
    x = 1 
    return x+y 

#호출
print( func2(1) )

