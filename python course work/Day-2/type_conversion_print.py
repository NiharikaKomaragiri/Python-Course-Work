Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Type conversion
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=15.5
complex(b)
(15.5+0j)
bool(b)
True
int(b)
15
list(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
str(b)
'15.5'
str(a)
'10'
set(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
set(a,b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(a,b)
TypeError: set expected at most 1 argument, got 2
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
c='niharika'
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'niharika'
bool(c)
True
list(c)
['n', 'i', 'h', 'a', 'r', 'i', 'k', 'a']
tuple(c)
('n', 'i', 'h', 'a', 'r', 'i', 'k', 'a')
set(c)
{'r', 'a', 'i', 'k', 'n', 'h'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
complex(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
s='10'
complex(s)
(10+0j)
l=[1,2,3,4]
float(l)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
int(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
bool(l)
True
t=(1,2,3,4)
int(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
dict(t)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s={1,2,3,4}
int(s)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
list(s)
[1, 2, 3, 4]
tuple(s)
(1, 2, 3, 4)
str(s)
'{1, 2, 3, 4}'
dict(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d={1:1,2:2,3:3}
int(d)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
str(d)
'{1: 1, 2: 2, 3: 3}'
complex(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
list(d)
[1, 2, 3]
tuple(d)
(1, 2, 3)
set(d)
{1, 2, 3}
bool(d)
True
b=True
str(b)
'True'
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
a=10
b=10.2
c='python'
print(a,b,c)
10 10.2 python
print('a=',a,'b=',b,'c=',c)
a= 10 b= 10.2 c= python
print('a=',a,'b=',b,'c=',c,sep='')
a=10b=10.2c=python
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
10.2
c=
python
print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	10.2	c=	python
print('a=',a,'b=',b,'c=',c,sep='\t'end='\n\n')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	10.2	c=	python

println('niharika')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    println('niharika')
NameError: name 'println' is not defined. Did you mean: 'print'?
print\n('niharika')
SyntaxError: unexpected character after line continuation character
print('a=',a,'b=',b,'c=',c,sep='\t',end='@@@')
a=	10	b=	10.2	c=	python@@@
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n','name=',niharika)
SyntaxError: positional argument follows keyword argument
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n','name=')
SyntaxError: positional argument follows keyword argument
print(f'a: {a},b: {b},c: {c}')
a: 10,b: 10.2,c: python
print('a= %d b=%f c=%s'%(a,b,c))
a= 10 b=10.200000 c=python
print('a= %d b=%.2f c=%s'%(a,b,c))
a= 10 b=10.20 c=python
print(f'a: {},b: {},c: {}'.format(a,b,c))
SyntaxError: f-string: valid expression required before '}'
print(f'a: {} b: {} c: {}'.format(a,b,c))
SyntaxError: f-string: valid expression required before '}'
print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=python
KeyboardInterrupt
print('a={2} b={1} c={0}'.format(a,b,c))
a=python b=10.2 c=10
a=input("Enter the name")
Enter the name niharika
name
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    name
NameError: name 'name' is not defined
a
' niharika'
type(a)
<class 'str'>
age = input("Enter the age:")
Enter the age:21
age
'21'
age=int(input("Enter the age:"))
Enter the age:21
age
21
type(age)
<class 'int'>
name=str(input("Enter your name:"))
Enter your name:niharika
name
'niharika'
type(name)
<class 'str'>
gpa=float(input("Enter the gpa"))
Enter the gpa 8.5
type(gpa)
<class 'float'>
'niharika lohi vijay nani papa'.split()
['niharika', 'lohi', 'vijay', 'nani', 'papa']
names = input("Enter the names: ").split()
Enter the names: niharika lohi nani vijay
names
['niharika', 'lohi', 'nani', 'vijay']
age = input("Enter the ages:").split()
Enter the ages:21 22 23 24
age
['21', '22', '23', '24']
list(map(int,input("Enter the ages: ").split()))
Enter the ages: 21 16 27 18 19
[21, 16, 27, 18, 19]
>>> list(map(float,input("Enter the ages: ").split()))
Enter the ages: 12 13 14 15 17
[12.0, 13.0, 14.0, 15.0, 17.0]
>>> age=list(map(int,input("Enter the ages: ").split()))
Enter the ages: 12 13 14 15 16
>>> age
[12, 13, 14, 15, 16]
>>> names=tuple(input("Enter the names: ").split()))
SyntaxError: unmatched ')'
>>> age=tuple(map(int,input("Enter the ages: ").split()))
Enter the ages: 12 13 14 15
>>> age
(12, 13, 14, 15)
>>> age=set(map(int,input("Enter the ages: ").split()))
Enter the ages: 12 13 14 15
>>> age
{12, 13, 14, 15}
>>> age=set(map(float,input("Enter the ages: ").split()))
Enter the ages: 45 46 47 48
>>> age
{48.0, 45.0, 46.0, 47.0}
>>> age=set(input().split())
niharika nihai 
>>> age
{'niharika', 'nihai'}
>>> a=eval(input())
[1,2,3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> a=eval(input())
(1,2,3,4,5)
>>> a
(1, 2, 3, 4, 5)
>>> a=eval(input("Enter the dict: "))
Enter the dict: {no:1,name:niha,group:cse}
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    a=eval(input("Enter the dict: "))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'no' is not defined
>>> a=eval(input("Enter the dict: "))
Enter the dict: {2:3,4:5}
>>> a
{2: 3, 4: 5}
