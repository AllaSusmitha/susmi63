
a=int(input())
list=[int(x) for x in input().split()]
for i in range(0,a):
        sum=0
        sum1=0
        for x in range(0,i):
                sum=sum+list[x]
        for y in range(i+1,n):
                sum1=sum1+list[y]
        if(sum==sum1):
                print('yes')
                break
        elif(i==(a-1)):
                print('no')


