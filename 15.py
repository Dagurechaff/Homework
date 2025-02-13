def S(a, b, c):
	return (a * b) > c
def f(A):
	for x in range(1, 1000):
		for y in range(1, 1000):
			if not(S(x, y, A + 13) or S(28, y, 520) or S(x, 25, 800)):
				return 0
	return 1
mx = -10 ** 23
for A in range(-100, 1000):
	if f(A):
		mx = A
print(mx)