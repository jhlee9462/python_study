# 값을 기준으로 정렬하기
# 1. 딕셔너리에서 items 메서드를 실행한다.
# 2. 튜플을 활용해 키와 값을 분리한다.
# 3. 키와 값의 위치를 바꾼 리스트를 생성한다.
# 4. 생성된 리스트를 정렬한다.

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp)
print(tmp)

# 내림차순으로 정렬하고 싶다면 다음과 같이 sorted 함수에 reverse 옵션을
# True로 설정하면 됩니다.
tmp = sorted(tmp, reverse=True)
print(tmp)