
#Factors using generators
#like - 12-1 2 3 4 6 12
def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

def gen(res):
    for i in res:
        yield i

r=factors(89)
g=gen(r)
for i in range(len(r)):
    print(next(g))
    
output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
1
89


#reversing the list using generator
    
def generator(res):
    for i in range(len(res)-1,-1,-1):
        yield res[i]
l=eval(input())
g=generator(l)
for i in range(len(l)):
    print(next(g),end=' ')

output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
input-'python','java','flask','mysql','django'
django mysql flask java python
#upper case conversion
def gen(l):
    for i in l:
        yield i.upper()
        
l=['python','java','flask','mysql','django']

g=gen(l)
for i in range(len(l)):
    print(next(g))

output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
PYTHON
JAVA
FLASK
MYSQL
DJANGO

#Even numbers

#logic for getting even number
def even(l):
    return list(filter(lambda i:i%2==0,l))

#yielding
def gen(l):
    for i in l:
        yield i
        
#input()
l=list(map(int,input().split(',')))

#calling the functions
e=even(l)
g=gen(e)
for i in range(len(e)):
    print(next(g))


output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
input-24,56,12,34,56,11,13,15,17,90,99,45,23,22,12,78
24
56
12
34
56
90
22
12
78


# Generator function
def countdown_gen(n):
    while n >= 0:
        yield n
        n -= 1

# Example
g = countdown_gen(5)

for i in g:
    print(i)

Output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
5
4
3
2
1
0

    
#Fibonacci Series Generator
def fib_gen(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b

g = fib_gen(7)

for i in g:
    print(i)

Output
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/yields and modules.py
0
1
1
2
3
5
8























