line = 'From stephen.marquard@uct.ac.za Sat Jan5 09:14:16 2008'
# line 에 uct.ac.za 만 추출하는 방법을 찾아 보도록 하겠습니다.
words = line.split()
# words 는 해당 라인을 빈칸을 구분자로 하여 리스트로 저장됩니다.
print(words[1])
# stephen.marquard@uct.ac.za
email = words[1]
address = email.split('@')
print(address)
print(address[1])