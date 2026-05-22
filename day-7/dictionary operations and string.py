Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={1:1,2:2,3:3,4:5}
d
{1: 1, 2: 2, 3: 3, 4: 5}
d.get(7)
d
{1: 1, 2: 2, 3: 3, 4: 5}
d.keys()
dict_keys([1, 2, 3, 4])
d.values()
dict_values([1, 2, 3, 5])
d.items()
dict_items([(1, 1), (2, 2), (3, 3), (4, 5)])
len(d)
4
min(d)
1
max(d)
4
d
{1: 1, 2: 2, 3: 3, 4: 5}
d.get(3)
3
d.get(4)
5
sorted(d)
[1, 2, 3, 4]
d
{1: 1, 2: 2, 3: 3, 4: 5}
d.setdefault(7,0)
0
d.sort()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d.sort()
AttributeError: 'dict' object has no attribute 'sort'
#set
s=set()
s
set()
s={2,3,4,5,88,93,34,34,34,13,344}
s
{2, 3, 4, 5, 34, 344, 13, 88, 93}
s=set()
s
set()
s.add(1)
s
{1}
s.add(1.1)
s
{1, 1.1}
s.add('string')
s
{1, 1.1, 'string'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2,3))
s
{1, (1, 2, 3), 1.1, 'string'}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: unhashable type: 'set'
s.add('False')
s
{1, 1.1, (1, 2, 3), 'string', 'False'}
s.add({1:2,2:3}]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
s.add({1:2,2:3})
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.add({1:2,2:3})
TypeError: unhashable type: 'dict'
s
{1, 1.1, (1, 2, 3), 'string', 'False'}
s.add(2+3j)
s
{1, 1.1, (1, 2, 3), (2+3j), 'string', 'False'}
1 in s
True
2 not in s
True
a={1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
b={2,3,4,5,6}
b
{2, 3, 4, 5, 6}
a+b
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a | b
{1, 2, 3, 4, 5, 6}
a&b
{2, 3, 4, 5, 6}
a-b
{1}
b-a
set()
a ^ b
{1}
{1,2}<a
True
{3,7}<a
False
{1,2,3,4,5,6,7}>a
True
{1,3,4}>a
False
x={1,2}
y={3,4}
x.disjoint(y)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x.disjoint(y)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
x.isdisjoint(y)
True
a.union(b)
{1, 2, 3, 4, 5, 6}
max(a)
6
min(a)
1
len(a)
6
sorted(a)
[1, 2, 3, 4, 5, 6]
sum(a)
21
a.add(7)
a.add(80)
a
{80, 1, 2, 3, 4, 5, 6, 7}
a.update({67,89,10})
>>> a
{1, 2, 3, 4, 5, 6, 7, 67, 10, 80, 89}
>>> a.pop()
1
>>> a
{2, 3, 4, 5, 6, 7, 67, 10, 80, 89}
>>> a.pop()
2
>>> a.clear()
>>> a
set()
>>> a.copy()
set()
>>> a={1,2,3,4,5,6,7,9}
>>> a
{1, 2, 3, 4, 5, 6, 7, 9}
>>> b={4,7,8,5,2,19}
>>> b
{2, 19, 4, 5, 7, 8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 19}
>>> a
{1, 2, 3, 4, 5, 6, 7, 9}
>>> b
{2, 19, 4, 5, 7, 8}
>>> a.updateunion(b)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.updateunion(b)
AttributeError: 'set' object has no attribute 'updateunion'
>>> a.union_update(b)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.union_update(b)
AttributeError: 'set' object has no attribute 'union_update'
>>> a.intersection_update(b)
>>> a
{2, 4, 5, 7}
>>> b
{2, 19, 4, 5, 7, 8}
>>> n=int(input())
if(n%2==0):print("even")
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    n=int(input())
ValueError: invalid literal for int() with base 10: 'if(n%2==0):print("even")'
