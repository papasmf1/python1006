# 정적메서드.py
class MyCalc(object):
    #어노테이션:살아있는 주석
    @staticmethod
    def my_add(x,y):
        return x+y
    #인스턴스 메서드
    def methodA(self):
        print("인스턴스 메서드 실행")

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

#인스턴스를 생성
calc = MyCalc() 
calc.methodA() 
