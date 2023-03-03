purse = dict()  # 또는 purse = {} 와 같이 생성할 수도 있습니다.
purse['money'] = 12  # 'money'라는 키에 12 라는 값 연결
purse['candy'] = 3  # 'candy'라는 키에 3 이라는 값 연결
purse['tissues'] = 75  # 'tissues'라는 키에 75 라는 값 연결

print(purse) # 항상 입력한 순서대로 출력되는 것은 아님

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)