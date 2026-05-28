
#System
import sys

print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
print()
sys.exit()

print('end')

#platform
import platform

print(platform.system())
print()
print(platform.release())
print()
print(platform.processor())

#Mathematics Functions
import math

print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.pow(2,3))

print(math.ceil(12.00009))#ceil-It tends to upper value
print(math.ceil(12.5))
print(math.ceil(-12.78))
print(math.floor(12.3))#floor-it tends to lower value
print(math.floor(-13.890))
print(math.floor(-34.999))

print(math.fabs(-123))#remove negative(-)
print(math.factorial(6))
      
print(math.gcd(44,12))#greater common divisor
print(math.log(2,10))
print(math.sin(20))
print(math.cos(30))
print(math.tan(50))

print(math.degrees(190))
print(math.radians(190))

Output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/import.py
3.141592653589793
2.718281828459045
4.0
8.0
13
13
-12
12
-14
-35
123.0
720
4
0.30102999566398114
0.9129452507276277
0.15425144988758405
-0.27190061199763077
10886.198107485641
10886.198107485641


#print random values
import random

#random.seed(12)#seed is used to give the same numbers again and again
print(random.random())#random value from range of 0 to 1
print(random.randint(1,3))#in range of 1,3(integer)
print(random.uniform(1,3))#uniform-float

l=['python','list','tuple','set']

print(random.choice(l))#print one choice
print(random.choices(l,k=2))#print 2 choices

print("before:",l)
random.shuffle(l)
print("After:",l)


import collections

s='pyhton programming'
#instead of writing a code to know the count of letter/value 
print(collections.Counter(s))#counter is used to know the value count

#int=collections.defaultdict(int)#int default value 
d=collections.defaultdict(str)#string default value
for i in s:
    d[i]+=i
print(d)
d={}

Output
#string
Counter({'p': 2, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'm': 2, 'y': 1, 'h': 1, 't': 1, ' ': 1, 'a': 1, 'i': 1})
defaultdict(<class 'str'>, {'p': 'pp', 'y': 'y', 'h': 'h', 't': 't', 'o': 'oo', 'n': 'nn', ' ': ' ', 'r': 'rr', 'g': 'gg', 'a': 'a', 'm': 'mm', 'i': 'i'})

#integer
Counter({'p': 2, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'm': 2, 'y': 1, 'h': 1, 't': 1, ' ': 1, 'a': 1, 'i': 1})
defaultdict(<class 'int'>, {'p': 2, 'y': 1, 'h': 1, 't': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1})


d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.popleft()
d.append(70)
d.append(89)
d.appendleft(10)

print(d)

Output
[10,70,89]


from itertools import combinations,permutations

print(list(combinations('ABCD',3)))
print(list(permutations('ABCD',3)))


Output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/import.py
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'),
 ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'),
 ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'),
 ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]





















