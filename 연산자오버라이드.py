#연산자 오버로드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	# + 연산자(object클래스 정의)
	def add(self, num):
		self.Num += num
	# - 연산자의 의미를 정의 
	def remove(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100)
print(n.Num)
n.remove(30)
print(n.Num)
