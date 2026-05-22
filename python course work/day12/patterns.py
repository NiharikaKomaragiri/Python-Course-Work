'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()

for row in range(5):
    for col in range(row+1):
        print('*',end=' ')
    print()

n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()

n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()

n=int(input("Enter the size:"))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        print(int(col%2==0),end=' ')
    print()

n=int(input())
for row in range(n):
    for col in range(n):
        print(int(col%2!=0),end=' ')
    print()

    
n=int(input())
for row in range(n):
    for col in range(n):
        print(int((row+col)%2==0),end=' ')
    print()

n=int(input())
for r in range(n):
    for c in range(n):
        if (r==0 or r==(n-1) or c==0 or c==(n-1)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())
for r in range(n):
    for c in range(n):
        if (r==0 or r==(n-1) or c==0 or c==(n-1)):
            print('*',end=' ')
        elif (r==2 or r==(n-3) or c==2 or c==(n-3)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''    
n=int(input())
for i in range(n)
























































