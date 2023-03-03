# 딕셔너리를 처리하는데 활용
# 딕셔너리의 items 메서드는 딕셔너리에 저장된 각 키와 값의 한 쌍을 튜플로
# 이루어진 리스트 형태로 만들어줍니다.
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)