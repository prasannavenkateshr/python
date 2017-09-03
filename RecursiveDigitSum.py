def toInts(s):
    y = map(int, list(str(s)))
    return sum(y)
n,k = map(int, raw_input().split(' '))
t = toInts(n) * k
while (len(str(t)) != 1): t = toInts(t)
print t
