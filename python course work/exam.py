'''
ch=input()
if ch.isalpha():
    print("alpha")
elif ch.isdigit():
    print("digit")
else:
    print("Special char")

    
n=input()
sum=0
for i in range(n):
    sum+=int(n)
    print(sum)


for i in range(1,51):
    if i%5==0:
        print(i,end=' ')

#Check if three lengths form an Equilateral, Isosceles, or Scalene
a,b,c=map(int,input().split())
if a==b==c:
    print("Equilateral")
elif a!=b!=c:
    print("Scalene")
else:
    print("Isosceles")
'''
#Classify a character as: vowel, consonant, digit, special character
vowel="AEIOUaeiou"
char=input()
if char in vowel:
    print("vowel")
elif char.isdigit():
    print("digit")
elif char.isalpha():
    print("consonant")
else:
    print("special character")

#Electricity bill calculator based on units used
n=int(input())



































    
