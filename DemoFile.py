# DemoFile.py

#파일에 쓰기(한글로 읽기나 쓰기를 할 경우 유니코드 스타일)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("한글\n데이터를쓰기\nabcd\n")
f.close()

#파일에서 읽기 
f = open("c:\\work\\demo.txt")
print( f.read() )
f.close() 


