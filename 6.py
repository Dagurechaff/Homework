from turtle import * 
screensize(10000, 10000)
pensize(4)
tracer(10)
left(90)
k = 5
for i in range(10):
	for j in range(3):
		forward(k * 10)
		right(90)
		forward(k * 10)
		right(270)
	right(90)
up()
print((30*30-10*10*3)*4)
done()