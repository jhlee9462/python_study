counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# 딕셔너리를 리스트로 변환하면 키로만 구성된 리스트를 얻을 수 있습니다.
print(list(counts))

# 딕셔너리의 keys 라는 메소드를 사용해도 같은 결과를 얻을 수 있습니다.
print(counts.keys())

# 값으로만 구성된 리스트를 얻으려면 values 라는 메소드를 사용하면 됩니다.
print(counts.values())