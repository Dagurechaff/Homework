def c(n, p):
    s = ''
    while n:
        s = str(n % p) + s
        n //= p
    return s

dig_max = 0
x = 7**200 - 7**50 + 1
n = 7**500 + 7**200 - 7**50 - x
s = c(n, 7)
print(sum(int(x) for x in s))