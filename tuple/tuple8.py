# 튜플을 활용해서 딕셔너리 정렬
# 키를 기준으로 정렬하기
# 1. 딕셔너리에서 items 메서드를 실행해 튜플로 이루어진 리스트 형태로 만든다.
# 2. 이 리스트를 sorted 함수로 정렬한다. 그러면 각각의 튜플의 왼쪽 값, 즉 키를 기준으로 정렬이 된다.
d = {'b': 1, 'a': 10, 'c': 22}

print(d.items())

print(sorted(d.items()))

for k, v in sorted(d.items()):
    print(k, v)