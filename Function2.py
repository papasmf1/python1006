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


