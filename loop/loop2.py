# loop 를 이용해서 개수 세기
zork = 0
print('Before',zork)
numbers = [9, 41, 12, 3, 74, 15]
for thing in numbers:
    zork = zork + 1
    print(zork, thing)
print('After',zork)

# loop 를 사용해서 합계 구하기
total = 0
for thing in numbers:
    total += thing
    print(total, thing)
print('After', total)

# loop 를 사용해서 평균 구하기
count = 0
sum = 0
print('Before', count, sum)
for value in numbers:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum / count)

# loop 를 사용하여 필터링 하기
for value in numbers:
    if value > 20:
        print('Large number', value)
print('After')

# 불리언 값을 사용하여 특정 값을 검색하기
found = False
print('Before', found)
for value in numbers:
    if value == 3:
        found = True
        print(found, value)
        break
print('After', found)

# 가장 작은 수를 찾는 코드 완성하기
smallest = None # None 은 다른 언어의 NULL 과 유사
print('Before')
for value in numbers:
    if smallest is None: # 변수의 Object 가 같을 때 True 를 리턴
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)