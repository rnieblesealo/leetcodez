from collections import Counter

s = "hello"
c = tuple(Counter(s).items())
print(c)
