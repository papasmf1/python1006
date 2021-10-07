# DemoPickle.py 

import pickle
#메모리에 있는 임시 객체를 백업을 받고 복구하기 
colors = ["red","blue","green"]

f = open("c:\\work\\colors", "wb")
pickle.dump(colors, f)
f.close() 

#삭제 
del colors 

#다시 복구하기
f = open("c:\\work\\colors", "rb")
colors = pickle.load(f)
print( colors )
f.close() 

