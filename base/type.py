ddd = 1 + 4
print(ddd) # 5 로 출력됩니다.

eee = 'hello ' + 'there'
print(eee) # hello there 로 출력됩니다.

i = 42
print(type(i)) # int 타입
f = float(i) # float 타입으로 변환
print(f) # 42.0 으로 출력
print(type(f)) # float 타입

sval = '123'
print(type(sval)) # str 타입

ival = int(sval)
print(type(ival)) # int 타입
print(ival + 1) # int 타입 간 연산이므로 오류 발생 x

nam = input('Who are you?')
print('Welcome', nam) # python3 의 print 에 , 를 통해 여러
# 인수들을 전달하면 알아서 띄어쓰기 후 다른 인수가 출력된다.

exp = 2 ** 2 # 거듭제곱 연산자
print(exp)