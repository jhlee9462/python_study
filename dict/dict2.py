counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print(counts)

"""
혹은 아래와 같이 not 을 사용해 해결
for name in names : 
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] += 1
print(counts)
"""
