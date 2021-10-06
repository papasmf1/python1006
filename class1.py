# class1.py 

#클래스를 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p1.print()
p2 = Person()
p2.name = "전우치"
p2.print()

#런타임시에 변수가 추가됨
#런타임은 코드가 실행되고 있다는 의미 
#디자인타임은 코딩을 하고 있다. 
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
