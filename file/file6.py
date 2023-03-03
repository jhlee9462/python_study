fhand = open('hello.txt')
for line in fhand :
    line = line.rstrip() # 오른쪽 공백 제거
    if line.startswith('Hello') :
        print(line)