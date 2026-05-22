'''
#Compare lengths of two strings
n=input()
m=input()
if len(n)==len(m):
    print("both are having same length")
elif len(n)<len(m):
    print("Second string is longer")
else:
    print("First string is longer")


#Check if a number is within a specific range (50 to 100) and divisible by 5
n=int(input())
if n in range(50,100):
    if n%5==0:
        print("in range and divisible by 5")
else:
    print("out of range")

#Validate if a password length is strong (8 or more characters)
n=8
password=input()
if password<=n:
    print("strong password")
else:
    print("setup again")

#Check if sum of two numbers is even
n=int(input())
m=int(input())
sum=n+m
print(sum)
if sum%2==0:
    print("Sum is even")
else:
    print("Sum is not even")

#Check if the character is a special symbol (!, @, #, etc.)
char="!,@,#,$,%,*"
n=input()
if n in char:
    print("Special character")
else:
    print("not a special char")

#16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)

temp=int(input())
if temp<15:
    print("cold")
elif temp<30:
    print("moderate")
else:
    print("hot")

#17. Check if a number lies outside the range 10 to 50
num=int(input())
if num in range(10,50):
    print("In range")
else:
    print("Outside the range")
'''

    
    
































