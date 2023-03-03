# 튜플은 리스트와 굉장히 비슷합니다. 단지 대괄호 대신 소괄호를 사용했다는 정도
# 리스트와 같이 순서가 있어서 인덱스로 접근이 가능하고, 최대값도 찾을 수 있습니다
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
#Joseph
y = (1, 9, 2)
print(y)
# (1, 9, 2)
print(max(y))
# 9

# 뿐만 아니라, for 반복문에서 반복을 시키면 리스트와 같이 원소를 순서대로
# 출력해줍니다.
for iter in y:
    print(iter)