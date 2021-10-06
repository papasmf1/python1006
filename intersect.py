# intersect.py
# 교집합을 리턴하는 함수
def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#함수를 호출
list1 = "SPAM"
list2 = "HAM"
#디버깅할 때 중지점을 만나면 브레이크 
print(intersect(list1, list2))
