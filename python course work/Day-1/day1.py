Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
myvar=10
myvar
10
Myvar=20
Myvar
20
_myvar=90
_myvar
90
my@var=10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
if=80
SyntaxError: invalid syntax
1myvar=5
SyntaxError: invalid decimal literal
my var=50
SyntaxError: invalid syntax
a=10
a
10
A=20
A
20
#single line comment
'''
multiple
line comments
in the code
KeyboardInterrupt
a=b=c=d=10
a
10
b
10
c
10
a,b,c,d=10,20,30,40
b
20
d
40
c
30
a,b=b,a #swapping
a
20
b
10
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

===================================================================== RESTART: Shell ====================================================================
a=10
type(a)
<class 'int'>
b=8.59
type(b)
<class 'float'>
>>> c=2+5i
SyntaxError: invalid decimal literal
>>> c=2+4j
>>> c
(2+4j)
>>> type(c)
<class 'complex'>
>>> s="Niharika"
>>> id(s)
2090805065328
>>> n=1,2,3,4
>>> id(n)
2090804614208
>>> n.append(5)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    n.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> n=[1,2,3,4]
>>> id(n)
2090805087744
>>> n.append(5)
>>> n
[1, 2, 3, 4, 5]
>>> id(n)
2090805087744
>>> type(n)
<class 'list'>
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> s=set()
>>> type(s)
<class 'set'>
>>> d={'name':'niharika','course':'pfs','batch':53}
>>> type(d)
<class 'dict'>
>>> d
{'name': 'niharika', 'course': 'pfs', 'batch': 53}
>>> d=None
>>> type(d)
<class 'NoneType'>
>>> a=False
>>> type(a)
<class 'bool'>
