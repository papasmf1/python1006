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
    #생성자 메서드에서 기본값을 지정하면 된다. 
    def __init__(self, name="", phoneNumber="", subject="", studentID=""):
        #부모의 생성자 메소드를 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 덮어쓰기한 경우(오버라이드, 재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID {1})".format(
            self.subject, self.studentID))
    #가변인자 처리
    def union(self, *ar):
        result = []
        for item in ar:
            for x in item:
                if x not in result:
                    result.append(x)
        return result 

#인스턴스를 생성 
p = Person("전우치", "010-222-1234")
s1 = Student("이순신", "010-111-1234", "컴공")
s2 = Student("박문수", "010-123-1234", "중어중문", "02")
# 다중라인으로 주석처리: ctrl + / 
# print( p.__dict__ )
# print( s.__dict__ )
p.printInfo()
s1.printInfo()
s2.printInfo() 
print( s2.union("HAM","SPAM") )
print( s2.union("HAM","SPAM","EGG") )

