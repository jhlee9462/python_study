str = 'X-DSPAM-Confidence: 0.8475'

# python3 은 주석처리 기호가 해시이지만 vsc 에서 ctrl + / 로도 주석처리 단축이 잘 된다!

ipos = str.find(':')
# print(ipos)
piece = str[ipos + 2:]
# print(piece)
value = float(piece)
# print(value)
print(value + 42.0)