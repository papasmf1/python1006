# 부모 클래스 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 
class Student(Person):
    #상속받은 __init__를 사용할 수 없어서 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 생성자 메소드를 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

#인스턴스를 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# 다중라인으로 주석처리: ctrl + / 
# print( p.__dict__ )
# print( s.__dict__ )
p.printInfo()
s.printInfo()

