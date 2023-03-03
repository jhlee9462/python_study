counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    # name 이 counts 에 존재한다면 name 을 불러오고 아니라면 0 이라는 
    # 값을 가지는 name 키를 추가
    counts[name] = counts.get(name, 0) + 1
print(counts)