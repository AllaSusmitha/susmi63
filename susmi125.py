N=int(input())
if N <= 1000:
	if N > 1:
		for i in range(2,N):
			if N % i == 0:
				print("yes")
				break
		else:
			print("no")
	else:
		print("yes")
else:
	print("yes")
