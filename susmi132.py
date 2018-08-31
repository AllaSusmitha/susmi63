st=raw_input()
a,b=0,0
for i in st:
	if i.isdigit():
		b+=1
	else:
		a+=1
if (b>0 and a>0):
	print "Yes"
else:
	print "No"
		
