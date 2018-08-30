n,m=map(int,raw_input().split())
x=n*m
for i in range (1,x):
	y=i*i
	if y==x:
		print("yes")
		break
else:
	print("no")
	
