a = []
b = []
c = a

result = (a is b)
print(result) # False

result = (a is c)
print(result) # True

result = (b is c)
print(result) # False

result = (a == b)
print(result) # True

result = (a == c)
print(result) # True

result - (b == c)
print(result) # True