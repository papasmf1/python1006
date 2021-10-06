class Person:
    pass

class Bird:
    pass

#상속을 연습 
class Student(Person):
    pass

#인스턴스를 나열해서 생성 
p, s = Person(), Student()

#전역 함수 
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))