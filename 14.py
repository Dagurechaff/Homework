def to_sum_7(n):
	s = ''
	while n != 0:
		s += str(n % 7)
		n //= 7
	return s[::-1]

n = 7 ** 500 + 7 ** 200 - 7 ** 50
s = to_sum_7(n)
print(6 * (len(s) - 1))