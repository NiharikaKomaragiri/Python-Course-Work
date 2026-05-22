'''
n=int(input())
for i in range(1,n+1):
    for j in range(n):
        if (i>j):
            print(i,end='')
    print()

n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print('',end='')
        
    for k in range(i):
        print('*',end='')
    print()


n = int(input("Enter rows: "))

for i in range(1, n+1):

    # spaces
    for j in range(n-i):
        print("  ", end="")

    # stars
    for k in range(i):
        print(" *", end="")

    print()
    

n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print('  ',end='')
    for k in range(2*i-1):
        print('* ',end='')
    print()
        

n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()

n=int(input())
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()


n=int(input())

for i in range(n):
    for j in range(i+1):
        print(i*j,end=' ')
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()

        
n=int(input())
c=0
for i in range(n):
    for j in range(i+1):
        print((chr(65+c)),end=' ')
        c+=1
    print()

l=[23,45,12,28,90,67,101,56,78]
n=int(input())
for i in range(len(l)):
    if l[i]==n:
        print('Element found at:',i)

l=[23,45,12,28,90,67,101,56,78]
i=0
while i<len(l):
    if l[i]==67:
        print(l[i],"found at index:",i)
        break
    i+=1
else:
    print('not found')

l=[23,45,12,28,90,67,101,56,78]
i=0
m=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)


l=[23,45,12,28,90,67,101,56,78]
i=0
a=len(l)-1
while i<=a:
    if i==a:
        print(l[i])
    else:
        
        add=l[i]+l[a]
        print(add)
    i+=1
    a-=1
'''














































