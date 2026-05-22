Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
for i in s:
...     print(i)
... 
p
y
t
h
o
n
>>> l=[1,2,3,4,5]
>>> for i in l:
...     print(l)
... 
...     
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
>>> print(i)
5
>>> l=[1,2,3,4,5]
>>> for i in l:
...     print(i)
... 
...     
1
2
3
4
5
>>> t=(1,2,3,4,5)
>>> for i in t:
...     print(i)
... 
...     
1
2
3
4
5
>>> s='python'
>>> for i in s:
...     
KeyboardInterrupt
>>> s='python'
>>> for i in enumerate(s):
...     print(i)

    
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
s[0]
'p'
print(i[0],i[1])
5 n
l=[1,23,4,5,6,6]
for i in enumerate(l):
    print(i[0],i[1])

    
0 1
1 23
2 4
3 5
4 6
5 6
t=('py','cse','.net','node.js')
for i in enumerate(t)
SyntaxError: expected ':'
t=('py','cse','.net','node.js')
for i in enumerate(t):
    print(i[0],i[t],i)

    
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    print(i[0],i[t],i)
TypeError: tuple indices must be integers or slices, not tuple
t=['py','cse','.net','node.js']
for i in enumerate(t):
    print(i[0],i[t],i)

    
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(i[0],i[t],i)
TypeError: tuple indices must be integers or slices, not list
t=('py','cse','.net','node.js')
for i in enumerate(t):
    print(i[0],i[1],i)

    
0 py (0, 'py')
1 cse (1, 'cse')
2 .net (2, '.net')
3 node.js (3, 'node.js')
d={'k1':'v1','k2':'2','k3':'3'}
for i in range(1,11)
SyntaxError: expected ':'
for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
for i in range(2,21,2):
    print(i)

    
2
4
6
8
10
12
14
16
18
20
for i in range(5,51,5):
    print(i,end='')

    
5101520253035404550
for i in range(10,0,-1)
SyntaxError: expected ':'
for i in range(10,0,-1):
    print(i,end=' ')

    
10 9 8 7 6 5 4 3 2 1 
for i in range(1,100,2)
SyntaxError: expected ':'
for i in range(1,100,2):
    print(i,end=' ')

    
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 

============================== RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/control statements.py ==============================
Enter the pin:2345
Invalid pin
Enter the pin:12345
Invalid pin
Enter the pin:2345
Invalid pin
Enter the pin:12345
Invalid pin
Enter the pin:23456
Invalid pin
try after sometime

============================== RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/control statements.py ==============================
Enter the pin:23
Invalid pin
Enter the pin:123
Invalid pin
Enter the pin:1234
unlock phone
