def prostc(a):
	for i in range(2, int(a ** 0.5) + 1):
		if a % i == 0:
			return 0
	return 1
prost = []
for i in range(2, 100):
	if prostc(i):
		prost.append(i)
def t(a):
	global prost 
	for i in prost:
		if i > a:
			return i
def v(a, b):
	if a == 33:
		return 0
	if a == b:
		return 1
	if a > b:
		return 0
	return v(a + 2, b) + v(t(a), b)

print(v(2, 14) * v(14, 45))