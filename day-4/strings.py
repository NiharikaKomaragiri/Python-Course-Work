Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
s
'python'
type(s)
<class 'str'>
s=''
s
''
a='python'
a
'python'
id(a)
2289485463200
a=a+'language'
a
'pythonlanguage'
id(a)
2289487940592
fname='abc'
lname='xyz'
fname+lname
'abcxyz'
fname*10
'abcabcabcabcabcabcabcabcabcabc'
'*'*30
'******************************'
'niharika'*10
'niharikaniharikaniharikaniharikaniharikaniharikaniharikaniharikaniharikaniharika'
n='niharika vijay'
names[0]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names[0]
NameError: name 'names' is not defined. Did you mean: 'fname'?
n[0]
'n'
n[-1]
'y'
names='niharika' 'vijay'
names[0]
'n'
names[9]
'i'
names[8]
'v'
names[7]
'a'
names[-9]
'r'
names
'niharikavijay'
names[:8]
'niharika'
names[:16]
'niharikavijay'
names[9:14]
'ijay'
names[8:15]
'vijay'
names[-1:-5]
''
names[-1:5]
''
names[::-1]
'yajivakirahin'
names[:-1]
'niharikavija'
names[-9:-1]
'rikavija'
names[-5:-1]
'vija'
names[-5]
'v'
names[-5:]
'vijay'
names='lohisree prasanna prabhu niharika vijay'
names[8:]
' prasanna prabhu niharika vijay'
names[0:8]
'lohisree'
names[8:16]
' prasann'
names[8:17]
' prasanna'
names[17:23]
' prabh'
names[17:24]
' prabhu'
names[24:33]
' niharika'
names[33:39]
' vijay'
names[-1:-5]
''
names[-5:]
'vijay'
names[-13:]
'iharika vijay'
names[-6:-14]
''
names[-14:-6]
'niharika'
'niharika' in names
True
'kumar' not in names
True
family=names
family
'lohisree prasanna prabhu niharika vijay'
id(names)
2289531084496
family(id)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    family(id)
TypeError: 'str' object is not callable
id(family)
2289531084496
names is family
True
names is not family
False
l=names
l
'lohisree prasanna prabhu niharika vijay'
l.split()
['lohisree', 'prasanna', 'prabhu', 'niharika', 'vijay']
l[::-1]
'yajiv akirahin uhbarp annasarp eersihol'
l[::1]
'lohisree prasanna prabhu niharika vijay'
len(l)
39
sorted(l)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'e', 'e', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'j', 'k', 'l', 'n', 'n', 'n', 'o', 'p', 'p', 'r', 'r', 'r', 'r', 's', 's', 'u', 'v', 'y']
order('y')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    order('y')
NameError: name 'order' is not defined
ord('y')
121
chr(255)
'ÿ'
chr(150)
'\x96'
max(l)
'y'
min(l)
' '
ord('z')
122
ord('o')
111
char(100)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    char(100)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(100)
'd'
names='
KeyboardInterrupt
names='Lohisree Prasanna Prabhu'
names
'Lohisree Prasanna Prabhu'
names.upper()
'LOHISREE PRASANNA PRABHU'
names.lower()
'lohisree prasanna prabhu'
l=names
l.capitalize()
'Lohisree prasanna prabhu'
l.title()
'Lohisree Prasanna Prabhu'
l.swapcase()
'lOHISREE pRASANNA pRABHU'
"wertyuio".casefold()
'wertyuio'
names.swapcase()
'lOHISREE pRASANNA pRABHU'
names.center(50,'-')
'-------------Lohisree Prasanna Prabhu-------------'
names.center(40,'.')
'........Lohisree Prasanna Prabhu........'
names.ljust(30,'-')
'Lohisree Prasanna Prabhu------'
names.rjust(30,'-')
'------Lohisree Prasanna Prabhu'
names
'Lohisree Prasanna Prabhu'
names.ljust(8,'-')
'Lohisree Prasanna Prabhu'
'5'.zfill(5)
'00005'
'12345567'.zfill(20)
'00000000000012345567'
'23456'.zfill(2)
'23456'
names
'Lohisree Prasanna Prabhu'
names.find('N')
-1
names.find('L')
0
names.find('v')
-1
names.find('P')
9
>>> names.rfind('P')
18
>>> names.lfind('r')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    names.lfind('r')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
>>> names.rfind('r')
19
>>> names.index('a')
11
>>> names.rindex('P')
18
>>> names.index('z')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    names.index('z')
ValueError: substring not found
>>> names.count('a')
4
>>> names.count('n')
2
>>> names.count('o')
1
>>> names.count('z')
0
>>> names
'Lohisree Prasanna Prabhu'
>>> names.replace('a','1')
'Lohisree Pr1s1nn1 Pr1bhu'
>>> names.replace('lohisree','niharika')
'Lohisree Prasanna Prabhu'
>>> names.replace('Lohisree','Niharika')
'Niharika Prasanna Prabhu'
>>> names.replace('Niharika','')
'Lohisree Prasanna Prabhu'
>>> names.replace('Prabhu','')
'Lohisree Prasanna '
>>> names.replace('Lohisree','')
' Prasanna Prabhu'
>>> names.replace('aeiou','12')
'Lohisree Prasanna Prabhu'
>>> names.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> names.translate(names.maketrans('aeiou','12345'))
'L4h3sr22 Pr1s1nn1 Pr1bh5'
