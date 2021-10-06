# DemoContinueBreak.py
lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue---")

for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))


#수열함수 연습
print( list(range(10)) )
print( list(range(1,11)) )
for i in range(5):
    print(i)

print( list(range(2000,2022)) )


#리스트 컴프리헨션
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print( result )

test = ("apple","kiwi","orange")
print( [len(i) for i in test] )

d = {100:"apple", 200:"orange"}
print( [v.upper() for v in d.values()] )

#필터링을 하는 함수를 사용 
def getBiggerThan20(i):
    return i>20 

lst = [20, 30, 40]
#내장 함수중에 함수의 인자(파라메터로 함수를 호출)
iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print(i)


