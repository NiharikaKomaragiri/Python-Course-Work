'''
#init
while condi:
    #updation

a=[8,0,9,7,0,5,6,7,0,6]
while 0 in a:
    a.remove(0)
print(a)

while is condition is used for the updation of the list of numbers or len of the 
i=1
while i<=10:
    print(i,end=' ')
    i+=1

    
#Reverse even num
i=100
while i>=2:
    print(i,end=' ')
    i-=2

    
#Table
n=int(input("Enter the num:"))
i=1
while i<=10:
    print(f'{n}x{i}={n*i}')
    i+=1


i=1
while i<=10:
    if i==5:
        break
    print(i,end=" ")
    i+=1


i=1
while i<=10:
    i+=1
    if i==7:
        continue
    print(i,end=' ')

#sum of digits
n=int(input())
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)


#factorial
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#factors of the give number
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
    

n=input()
res=''
for i in n:
    res+=(chr(ord(i)+1))
print(res,end='')


n=input()
i=len(n)-1
while i>=0:
    print(n[i],i)
    i-=1
 
'''
#first non-repeating char
n=input()
for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("all are reapting")
    


























