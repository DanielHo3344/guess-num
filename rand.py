import random

r = random.randint(1,10)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == r :
		break