'''
#1.Print Numbers from 1 to N (Using for loop)
n=int(input())
for i in range(1,n+1):
    print(i,end=" ")

#2. Print Even Numbers from 1 to N (Using for loop)
n=int(input())
for i in range(2,n+1,2):
    print(i,end=' ')

#3. Sum of Numbers from 1 to N (Using for loop)
n=int(input())
sum=0
for i in range(1,n+1):
    print(i,end=' ')
    sum+=i
print('Sum=',sum)
   
#4. Print Odd Numbers from 1 to N (Using for loop)
n=int(input())
for i in range(1,n+1,2):
    print(i,end=' ')

#5. Find Factorial of a Number (Using for loop)
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
    

#6. Print Multiplication Table of N (Using for loop)
n=int(input())

for i in range(1,11):
    tab=(f"{n}x{i}={n*i}")
    print(tab)

#7. Check Prime Number (Using for loop)
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")

#8. Sum of Digits of a Number (Using while loop)
num=int(input())
sum=0

while num>0:
    a=num%10
    sum=sum+a
    num=num//10
print(sum)
'''       
# 9. Print Fibonacci Sequence up to N Terms (Using for loop)
n=int(input())

    

    




















        
