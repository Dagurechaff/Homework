def f(N):
	R = '0' * (8 - len(bin(N)[2:])) + bin(N)[2:]
	R = R[:2] + R[-2:]
	return int(R, 2)
for i in range(110):
	if f(i) == 7:
		print(i)