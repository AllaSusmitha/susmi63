n=input()
temp=n
for i in range(97,123):
    n=n.replace(chr(i),'')
    if(n==n[::-1]):
        print('YES')
        break
    n=temp
    if(i==122):
        print('NO')
    


