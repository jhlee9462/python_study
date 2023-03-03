# 리스트 컴프리헨션
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

tmp = sorted(tmp)
print(tmp)

# 다음의 코드는 정확히 위의 코드와 동일한 역할을 합니다.
print(sorted([(v, k) for k, v in c.items()]))
