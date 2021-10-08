# DemoStr.py 

strA = "python is very powerful"
print( len(strA) )
print( strA[0:6] )
print( strA[:6] )
print( strA[-3:] )

names = ["전우치","이순신","박문수"]
for name in names:
    print("안녕하세요 {0}님 가을이 다가옵니다.".format(name))
    print("=" * 40)

print("---str클래스의 멤버들---")
#print( dir(str) )


#str클래스의 메서드 사용
strA = "pytyon is very powerful"
print( len(strA) )
print( strA.capitalize() ) 
print( strA.endswith("ful") )
print( strA.count("p") )
print( strA.count("p", 7) )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

strB = "<<<  spam and ham  >>>"
print( strB )
print( strB.strip("<> ") )
result = strB.strip("<> ")
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print( lst )
print( ":)".join(lst) )






