words = 'Connect Foundation'

if 'Foundation' in words :
    # words.lower()
    # words[7] = '&' # python은 문자열 리터럴을 수정할 수 없다!
    words = words.replace(' Foundation', '&Foundation')
else :
    print(words)
print(words)

# or using this

words2 = words

parts = words2.split()
result = '&'.join(parts)

print(result)