fhand = open('hello.txt')
inp = fhand.read() # 단일한 하나의 문장으로 읽어 들이기
print(len(inp))
print(inp[:20])
# 각 문장에 대한 구분은 개행문자로 구분되어 있습니다