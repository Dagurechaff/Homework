with open('17333.txt') as file:
	s = [int(i) for i in file.read().strip().split()]

sr = (max(s) + min(s)) / 2
mxs = -1
c = 0
for i in range(len(s) // 2):
	if (s[i] > sr and s[-i - 1] < sr) or (s[i] < sr and s[-i - 1] > sr):
		c += 1
		mxs = max(mxs, s[i] + s[- i - 1])
print(c, mxs)


