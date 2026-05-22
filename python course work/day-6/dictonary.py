Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
sum(l)
15
all(l)
True
any(l)
True
any([1,4.7,0.0,{},(),[],False])
True
all([1,4.7,0.0,{},(),[],False])
False
all(['niharika',[7,8,9],3.455,True])
True
t=(1,2,3,,5)
SyntaxError: invalid syntax
t=(1,2,3,5)
t
(1, 2, 3, 5)
any(t)
True
all(t)
True
t.add(8)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.add(8)
AttributeError: 'tuple' object has no attribute 'add'
t.append(34)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.append(34)
AttributeError: 'tuple' object has no attribute 'append'
t.remove(3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.remove(3)
AttributeError: 'tuple' object has no attribute 'remove'
t=(1,1,1,2,3,4)
t
(1, 1, 1, 2, 3, 4)
t=(1.23,123,'python',[1,2,3,4],(4,5,6),{2:3,4:5},{1,2,3})
t
(1.23, 123, 'python', [1, 2, 3, 4], (4, 5, 6), {2: 3, 4: 5}, {1, 2, 3})
t(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t[3]
[1, 2, 3, 4]
t[3].append(5)
t[3]
[1, 2, 3, 4, 5]
a=(1,2,3,4,5)
z,x,c,v,b=a
z
1
x
2
v
4
t=(12,72,35)
id(t)
2519350567264
t=t+(2,3)
t
(12, 72, 35, 2, 3)
id(t)
2519322317184
t=('vijay','navitha','navi','navish')
t
('vijay', 'navitha', 'navi', 'navish')
t+('niharika','vinith')
('vijay', 'navitha', 'navi', 'navish', 'niharika', 'vinith')
t
('vijay', 'navitha', 'navi', 'navish')
t[4]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t[3]
'navish'
t[-1]
'navish'
t[0]
'vijay'
t[:3]
('vijay', 'navitha', 'navi')
t[::-1]
('navish', 'navi', 'navitha', 'vijay')
t
('vijay', 'navitha', 'navi', 'navish')
t[-2:-1:-3]
()
t[-1:-4:-1]
('navish', 'navi', 'navitha')
navish not in t
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    navish not in t
NameError: name 'navish' is not defined
'navish' not in t
False
'niharika' not in t
True
t=(1,2,3,3,3,3,4,4,5,6,6,6)
t
(1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6)
t.count(2)
1
t.count(3)
4
t.index(5)
8
t.index(9)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t.index(9)
ValueError: tuple.index(x): x not in tuple
max(t)
6
max(t)
6
min(t)
1
sorted(t)
[1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6]
sum(t)
46
len(t)
12
data={1:1,2:4,3:9,4:16}
data
{1: 1, 2: 4, 3: 9, 4: 16}
data={'ID':255,'Name':'niharika','skills':['python','html','css','java'],'gpa':8.5}
data
{'ID': 255, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
d[1]='int'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d[1]='int'
NameError: name 'd' is not defined. Did you mean: 'id'?
d[(1)]='integer'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d[(1)]='integer'
NameError: name 'd' is not defined. Did you mean: 'id'?
data
{'ID': 255, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
d={}
d[1]='integer'
d
{1: 'integer'}
d['string']='niharika'
d[False]='bool'
d[6+5j]='complex'
d[9.56]='float'
d
{1: 'integer', 'string': 'niharika', False: 'bool', (6+5j): 'complex', 9.56: 'float'}
data['ID']=105
data
{'ID': 105, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 'integer', 'string': 'niharika', False: 'bool', (6+5j): 'complex', 9.56: 'float'}
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3)]='tuple'
d
{1: 'integer', 'string': 'niharika', False: 'bool', (6+5j): 'complex', 9.56: 'float', (1, 2, 3): 'tuple'}
data
{'ID': 105, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
>>> 'ID' in data
True
>>> 'age' not in data
True
>>> data['skills']
['python', 'html', 'css', 'java']
>>> data['Name']
'niharika'
>>> data.get['ID']
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    data.get['ID']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> data.get('ID')
105
>>> data.get('age')
>>> data.get('age','age is not present')
'age is not present'
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> data
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> data={'ID': 105, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
>>> data
{'ID': 105, 'Name': 'niharika', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
>>> data['Name']='vijay'
>>> data
{'ID': 105, 'Name': 'vijay', 'skills': ['python', 'html', 'css', 'java'], 'gpa': 8.5}
>>> id(data)
2510971445056
>>> data['skills'].append('flask')
>>> data
{'ID': 105, 'Name': 'vijay', 'skills': ['python', 'html', 'css', 'java', 'flask'], 'gpa': 8.5}
>>> id(data)
2510971445056
>>> data['age']=21
>>> data
{'ID': 105, 'Name': 'vijay', 'skills': ['python', 'html', 'css', 'java', 'flask'], 'gpa': 8.5, 'age': 21}
>>> data.update({'ph':2345678900,'year':'2026','email':'@gmail.com'})
>>> data
{'ID': 105, 'Name': 'vijay', 'skills': ['python', 'html', 'css', 'java', 'flask'], 'gpa': 8.5, 'age': 21, 'ph': 2345678900, 'year': '2026', 'email': '@gmail.com'}
del data['skills']
data
