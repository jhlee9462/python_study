words2 = 'fisrt;second;third'
stuff2 = words2.split()
print(stuff2)
# ['first;second;third]
stuff2 = words2.split(';')
print(stuff2)
# ['first', 'second', 'third']
# 명시적으로 구분자를 넣어주지 않으면, 빈칸을 구분자로 인지하고 나누게 됩니다.