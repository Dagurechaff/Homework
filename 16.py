from sys import setrecursionlimit
setrecursionlimit(100000000)
def F(n):
	if n >= 3210:
		return 1
	return F(n + 3) + 7

def G(n):
	if n < 10:
		return n
	return G(n - 3) + 5

print(F(15) - G(3000))
	