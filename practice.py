#문자열 포맷
abc = '파이썬'
a = '자바'
print(f'{abc}') #문자열 포맷



#리스트
my_list = [1, 3.14, True, '문자열'] #리스트는 모든 자료형 포함가능
second_list = [121425, 45]
empty_list = []
print(my_list[0]) #인덱스 0값인 1이 출력됨
print(my_list[0:2]) #문자열 슬라이싱
print('문자열' in my_list) #my_list에 '문자열' 이 있을 시 불리안 형태로 출력
print(len(my_list)) #문자열의 길이(값의 개수)
my_list.append('정수') #리스트 가장 뒤에 값 추가
my_list.remove('정수') #리스트에서 특정 값을 삭제
my_list.extend(second_list) #리스트 더하기


#튜플 -> 수정불가. 읽기전용 리스트
my_tuple = (2, 4134, '문자열') #패킹
(num1, num2, str1) = my_tuple
#num1 = 2
#num2 = 4134
#str1 = '문자열'

numbers = (1, 2, 3, 4, 5)
(one, two, *others) = numbers #others 는 리스트
(one, *others, five) = numbers #others 는 리스트


#세트, 순서가 보장되지 않는다. -> 인덱스 사용 불가. 
#세트 = {값1, 값2, ...}


#딕셔너리 = {key1:value1, key2=value2, ...}
person = {
    '이름' : '어린씌',
    '나이' : 17
}
print(person['이름'])


def get_price(is_vip=False): # = 뒤에는 파라미터의 기본값
    if is_vip == True:
        return 10000
    else:
        return 15000
price1 = get_price() #15000 출력



f = open('list.txt', 'w', encoding='utf8')  
f.write('sfafdswnhsdkfid\n\n\nadkas\n')
f.close() 

class Abc:
    pass
b1 = Abc()
b1.name = '2131 '






############################################################################################
# 1. 변수와 자료형

# 1-1. 자료형
# 숫자 자료형 : 2가지로 나뉨. (정수: 3 7 -2, 실수: 0.5 3.14)
# 문자 자료형 : 따옴표가 붙은 모든 문자들. ("안녕하세요" "55")
# 불리안 자료형 : (True, False) 두가지로 나뉨

# 1-2. 변수 : 변하는 수.
# 값을 담는 상자
box = "Nothing"
box = "toy"
box = 4


# 참고
# 리스트 : 인덱스 값 자주 사용
    # 정의 : 변수명 = []
# 튜플
    # 정의 : 변수명 = ()
# 세트
    # 정의 : 변수명 = {}
# 딕셔너리
    # 정의 : 변수명 = {key1:value1, key2:value2...}
