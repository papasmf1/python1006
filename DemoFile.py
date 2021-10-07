# DemoFile.py

#파일에 쓰기(한글로 읽기나 쓰기를 할 경우 유니코드 스타일)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("한글\n데이터를쓰기\nabcd\n")
f.close()

#파일에서 읽기 
f = open("c:\\work\\demo.txt", encoding="utf-8")
#read()메서드는 str변수에 전체를 읽어오기
print( f.read() )


#리스트 형식으로 전체를 받기
print( f.tell() )
#다시 처음으로 돌아가~~ 
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )
print( f.readline(), end="" )


f.close() 

