# DemoRE.py 
#정규표현식:특정한 패턴을 찾기 
import re 

#서치함수: 검색결과를 매칭 객체로 리턴 
result = re.search("[0-9]*th", "  35th")
print( result )
print( result.group() )
#매치함수 
result = re.match("[0-9]*th", "  35th")
print( result )
#print( result.group() )

#어떤 단어가 포함되어있는지? 
print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )

#우편번호 찾기 
print( bool(re.search("\d{5}", "우리 동네는 52300")) )
print( bool(re.match("\d{5}", "우리 동네는 52300")) )


