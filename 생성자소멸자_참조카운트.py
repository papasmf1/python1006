# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    #생성자 메서드 
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    #소멸자 메서드 
    def __del__(self):
        print("Instance is deleted!")


#인스턴스 생성 
d = MyClass(10)
#인스턴스를 다 사용했으면 삭제도 가능 
#del d
#자동으로 가비지 컬렉션(GC) 서비스를 제공 
print("전체 코드 실행 종료")



