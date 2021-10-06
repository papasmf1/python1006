# DemoLoop.py

#소문자로 l s t 
lst = ["apple", 100, 3.14]

#반복구문
for item in lst:
    print(item, type(item))

#사전식구조
d = {"apple":100, "orange":200, "kiwi":300}

for item in d.items():
    print(item)

strA = "파이썬"
for char in strA:
    print(char)

#구구단 출력
#Outer 루프 
#디버깅모드로 실행할 때 중단점(Break Point)
for x in [2,3,4,5,6]:
    #입력 파라메터 처리 
    print("---{0}단---".format(x))
    #Inner 루프 
    for y in [1,2,3,4,5,6,7,8,9]:
        #포지션(위치를 지정): 0, 1, 2 
        print("{0} * {1} = {2}".format(x, y, x*y))


#이전 방식 
print("name:%s title:%s" % ("전우치", "대리") )

#디버깅은 논리적인 오류가 있는지를 살펴보기 
for x in [2,3,4,5,6]:
    #입력 파라메터 처리 
    print("---{0}단---".format(x))
    #Inner 루프 
    for y in [1,2,3,4,5,6,7,8,9]:
        #포지션(위치를 지정): 0, 1, 2 
        print("{0} * {1} = {2}".format(x, y, x*y))



