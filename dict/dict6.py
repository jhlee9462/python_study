jjj = {'chuck': 1, 'fred': 42, 'jan': 100}

# items 라는 메소드를 사용하면 튜플이라는 자료 구조 안에 키와 값이 쌍을
# 이루어 저장된 리스트가 반환됩니다.
print(jjj.items())

# 반복문을 사용하여 간결하게 딕셔너리에 저장된 키와 값을 출력할 수 있게
# 됩니다.
for aaa, bbb in jjj.items():
    print(aaa, bbb)
