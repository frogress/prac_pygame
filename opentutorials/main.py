#1 주석
#한 줄 주석
'''
안녕하세요
이것은
여러줄 주석입니다.
'''

#2 자료형
# 이름  : 아무개씨 <- 문자 자료형
# 주소  : 동구 <- 문자 자료형
# 전화번호  : 112 <- 정수 자료형
# 생년월일  : 0101 <- 정수 자료형

# 3.14 정수(X) 실수(O) == 실수 자료형
# True, False 불리안 자료형 boolean
is_dowon = False
if is_dowon == True:
    print("도원역을 제물포역으로 옮긴다")
print('10') # 문자 자료형 
print('나는 어제 \'내가 천재다\'라고 생각했다')


#3 변수
# 상자 안에 든 내용물
# 상자 = 변수
# 내용물 = 변수 안의 값
box = '장난감'
print(box)


#4 변수 이름 선언
# 문자 또는 _로 시작해야 된다.
# _80a = 34

# 문자, 숫자, _로만 구성되어야 한다.

# 공백 안되고 특수문자 안된다.

# 대소문자 구분한다
# number = 1
# Number = 2

# 소문자 단어를 쓰는게 좋다. 권장사항
# power_mode = 2


#5 자료 형변환
print(int('5')) # 5
print(float('3.14')) # 3.14
print(int(float('3.14'))) # 3 실수로 바꾼 후 정수로
print(int(float('3.8'))) # 3 무조건 내림
print(str(5)) # '5'
# int 정수
# float 실수
# str 문자

#6 연산자
# 산술 : +, -, *, /, %(나머지), //(몫), **(제곱)
            # 9 % 4 = 1
            # 9 // 4 = 2
# 비교 : >, >=, <, <=, ==, !=
            # 4 != 8 = True
# 논리 : and, or, not
            # print(not 3<5) -> False
# 멤버 : in, not in
            # print('c' in 'cat') -> True
            #print('c' not in 'cat') -> False


#7 불리안 자료형  bool(변수)
a = 'hello' # True 
b = '     ' # True
c = ''      # False
a = 1       # True 
b = -2       # True
c = 0       # False
bool(None)  # False, 값이 없다.



#8 인덱스와 슬라이싱
lang = 'PYTHON'
print(lang[0]) #P
print(lang[5]) #N
print(lang[-1]) #N
# [이상:미만:간격]
print(lang[0:4:1]) #PYTH



#9 문자열 처리
i = '사과'
print(len(i)) # 길이 출력 = 5


#10 문자열 포맷
print(f'안녕하세요 {i} 주세요.')


#11 사용자 입력
a = int(input("숫자 쳐 입력 하십쇼 : "))
print(a*2)