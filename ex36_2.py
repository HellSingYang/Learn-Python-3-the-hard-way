import time

def countdown(p, q):
	i = p
	j = q
	k = 0

	while True:

		#if j == -1:
		#	j = 59
		#	i -= 1
		if j > 9:
			print(str(k)+str(i)+":"+str(j), end = "\r")
		else:
			print(str(k)+str(i)+":"+str(k)+str(j), end = "\r")
			time.sleep(1)
		j -= 1
		if i == 0 and j == -1:
			break
	if i == 0 and j == -1:
		print("You are run out of time")
		time.sleep(10)
countdown(0, 10)
