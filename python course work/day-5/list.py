Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names'niharika vijay lohi sree'
SyntaxError: invalid syntax
names='niharika vijay lohi sree'
names
'niharika vijay lohi sree'
names.split()
['niharika', 'vijay', 'lohi', 'sree']
names.split(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    names.split(a)
NameError: name 'a' is not defined
names.split('a')
['nih', 'rik', ' vij', 'y lohi sree']
names.split(' ',2)
['niharika', 'vijay', 'lohi sree']
names.split(' ',1)
['niharika', 'vijay lohi sree']
names.append('prabhu','prasanna')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    names.append('prabhu','prasanna')
AttributeError: 'str' object has no attribute 'append'
names
'niharika vijay lohi sree'
names.partition(' ')
('niharika', ' ', 'vijay lohi sree')
'1.python.png'.partition('.')
('1', '.', 'python.png')
'1.python.png'.rpartition('.')
('1.python', '.', 'png')
'1.python.png'.lpartition('.')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    '1.python.png'.lpartition('.')
AttributeError: 'str' object has no attribute 'lpartition'. Did you mean: 'partition'?
''.join(l)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ''.join(l)
NameError: name 'l' is not defined
names
'niharika vijay lohi sree'
"".join(names)
'niharika vijay lohi sree'
''.join(names)
'niharika vijay lohi sree'
'-'.join(names)
'n-i-h-a-r-i-k-a- -v-i-j-a-y- -l-o-h-i- -s-r-e-e'
'free'.join(names)
'nfreeifreehfreeafreerfreeifreekfreeafree freevfreeifreejfreeafreeyfree freelfreeofreehfreeifree freesfreerfreeefreee'
h='   NNNNNNNNNNNNNNNNN   Nnnnnnnn    '
h.strip()
'NNNNNNNNNNNNNNNNN   Nnnnnnnn'
h.lstrip()
'NNNNNNNNNNNNNNNNN   Nnnnnnnn    '
h.rstrip()
'   NNNNNNNNNNNNNNNNN   Nnnnnnnn'
'heello'.encode()
b'heello'
b'hellooo'.decode()
'hellooo'
text='d'
text='smile 😁'.encode()
SyntaxError: multiple statements found while compiling a single statement
text2='smile 😁'.encode()
text2
b'smile \xf0\x9f\x98\x81'
b'smile \xf0\x9f\x98\x81'.decode()
'smile 😁'
'pyhton'.startswith('p')
True
'python.py'endswith('.py')
SyntaxError: invalid syntax
'python.py'.endswith('.py')
True
'sowm123'.isalpha()
False
'123456'.isalnum()
True
'123sdfg'.isalnum()
True
'rgdh'.islower()
True
'WESRT'.isupper()
True
'   '.isspace()
True
'Asdfgh Esdfgh sdfgh'.istitle()
False
'Aasdfg Sdfghj'.istitle()
True
'Sinhtfg'.isidentifier()
True
'345r6t'.isidentifier()
False
'ⅠⅢⅧ'.isnumeric()
True
'੦੩੮'.isdigit()
True
'↉⅛'.isdigit()
False
'↉⅛'.isnumeric()
True
'123s'isdecimal()
SyntaxError: invalid syntax
'123s'.isdecimal()
False
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
l=['wer',1,12.5,[1,2],(1,2),True,{1:1},{1,2,3},None]
l
['wer', 1, 12.5, [1, 2], (1, 2), True, {1: 1}, {1, 2, 3}, None]
l=[1,1,1,1]
l
[1, 1, 1, 1]
a=[1,2,3,4,5]
b=[2,3,4,5]
a+b
[1, 2, 3, 4, 5, 2, 3, 4, 5]
names
'niharika vijay lohi sree'
l=['niharika, vijay ,lohi, sree']
l[-4]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    l[-4]
IndexError: list index out of range
l[-3]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    l[-3]
IndexError: list index out of range
l
['niharika, vijay ,lohi, sree']
l[-2]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l[-2]
IndexError: list index out of range
l[1]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l[1]
IndexError: list index out of range
l=['niharika','lohi','koma','vijay']
l[2]
'koma'
l[-2]
'koma'
l[::2]
['niharika', 'koma']
l[::3]
['niharika', 'vijay']
l[0]
'niharika'
l[1]
'lohi'
l[7]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l[7]
IndexError: list index out of range
l[-3]
'lohi'
l[-1:-3]
[]
l[-1::]
['vijay']
l[-1:-4]
[]
l[::-1]
['vijay', 'koma', 'lohi', 'niharika']
l
['niharika', 'lohi', 'koma', 'vijay']
'komaragiri' not in l
True
'koma' not in l
False
'niha' in l
False
l=[]
l
[]
l=list()
l
[]
l=['niharika', 'lohi', 'koma', 'vijay']
l[0]
'niharika'
l[0]='komaragiri'
l
['komaragiri', 'lohi', 'koma', 'vijay']
l.append('kumar')
l
['komaragiri', 'lohi', 'koma', 'vijay', 'kumar']
l.delete('kumar')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l.delete('kumar')
AttributeError: 'list' object has no attribute 'delete'
l.del('kumar')
SyntaxError: invalid syntax
l.insert(1,'nivitha')
l
['komaragiri', 'nivitha', 'lohi', 'koma', 'vijay', 'kumar']
l.extend(['nikku','sonu','buji'])
l
['komaragiri', 'nivitha', 'lohi', 'koma', 'vijay', 'kumar', 'nikku', 'sonu', 'buji']
l.remove('buji')
l
['komaragiri', 'nivitha', 'lohi', 'koma', 'vijay', 'kumar', 'nikku', 'sonu']
l.remove(2)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l.remove(2)
ValueError: list.remove(x): x not in list
l.pop(3)
'koma'
l
['komaragiri', 'nivitha', 'lohi', 'vijay', 'kumar', 'nikku', 'sonu']
l.pop()
'sonu'
l
['komaragiri', 'nivitha', 'lohi', 'vijay', 'kumar', 'nikku']
l
['komaragiri', 'nivitha', 'lohi', 'vijay', 'kumar', 'nikku']
del l[0]
l
['nivitha', 'lohi', 'vijay', 'kumar', 'nikku']
>>> l.clear()
>>> l
[]
>>> l=['niharika', 'lohi', 'koma', 'vijay']
>>> sorted(l)
['koma', 'lohi', 'niharika', 'vijay']
>>> max(l)
'vijay'
>>> min(l)
'koma'
>>> len(l)
4
>>> l
['niharika', 'lohi', 'koma', 'vijay']
>>> l.index('lohi')
1
>>> l.index('niharikakomaragiri')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    l.index('niharikakomaragiri')
ValueError: list.index(x): x not in list
>>> l.count('niharika')
1
>>> l.sort()
>>> l
['koma', 'lohi', 'niharika', 'vijay']
>>> l.reverse()
>>> l
['vijay', 'niharika', 'lohi', 'koma']
>>> l=[1,2,3,4,5]
>>> m=l
>>> m.append(5)
>>> l
[1, 2, 3, 4, 5, 5]
>>> n=i.copy()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    n=i.copy()
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> n=l.copy()
>>> n.append(10)
>>> n
[1, 2, 3, 4, 5, 5, 10]
>>> l
[1, 2, 3, 4, 5, 5]
