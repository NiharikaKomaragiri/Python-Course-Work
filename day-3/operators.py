Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,c = [10,20,30]
a
10
b
20
c
30
a,b,c = list(map(int,input("Enter the integers : ").split()))
Enter the integers : 2 3 4 
a
2
b
3
c
4
email,password=input("Enter the email and password: ").spilt()
Enter the email and password: niharikakomaragiri@gmail.com  4567
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    email,password=input("Enter the email and password: ").spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
email,password=input("Enter the email and password: ").split()
Enter the email and password: abc@gmail.com 12345
email
'abc@gmail.com'
password
'12345'
a,b=tuple(map(int,input("Enter the integers: ").split()))
Enter the integers: 1 2 
a
1
b
2
a,b
(1, 2)
type(a,b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(a,b)
TypeError: type() takes 1 or 3 arguments
type(a)
<class 'int'>
t=(1,2,3,4)
type(t)
<class 'tuple'>
a=10
b=5
a+b
15
a-b
5
a/b
2.0
a*b
50
10/3
3.3333333333333335
10//3
3
a%b
0
2**3
8
8**9
134217728
a==b
False
a<b
False
a>b
True
a>=b
True
a<=b
False
a=!b
SyntaxError: invalid syntax
a!=b
True
2/5
0.4
2//5
0
2%5
2
a=40
a=a+20
a
60
a+=10
a
70
a-=10
a
60
a*=30
a
1800
a/=3
a
600.0
a//=4
a
150.0
a**=3
a
3375000.0
a%=2
a
0.0
45%5
0
4%2
0
5%4
1
2%9
2
4%9
4
a
0.0
a=20
a++
SyntaxError: invalid syntax
a=6
a%2==0 and a%3==0 and a%==6
SyntaxError: invalid syntax
a%2==0 and a%3==0 and a%6==6
False
a=20
a%2==0 and a%3==0 and a%==6
SyntaxError: invalid syntax
a%2==0 and a%3==0 and a%6==6
False
a%2==0 or a%3==0 or a%6==6
True
a%2==0 not a%3==0 not a%6==6
SyntaxError: invalid syntax
not a%2==0
False
a=67
not a%2==0
True
a=int(input("Enter the number"))
Enter the number12
if(a%2==0)
SyntaxError: expected ':'

===================================================================== RESTART: Shell ====================================================================
#str,list,tuple,set,dict
'p' in 'python'
True
'z' in 'python'
False
'i' not in 'python'
True
l=[1,2,3,4]
4 in l
True
9 not in l
True
1 not in l
False
t=(1,2,3,4)
1 not in t
False
s={2,3,4,5}
15 not in s
True
d={1:1,2:4,3:6,4:8}
6 in d
False
4 in d
True
d.keys()
dict_keys([1, 2, 3, 4])
d={'course:python','name:niha','batch:53'}
course in d
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    course in d
NameError: name 'course' is not defined
'course' in d
False
d={'name': 'niharika', 'course': 'pfs', 'batch': 53}
'name' in d
True
'batch' not in d
False
'niharika' not in d
True
>>> d.keys()
dict_keys(['name', 'course', 'batch'])
>>> t=(1,2,3,4,5)
>>> 1 is t
False
>>> a=(1,2,3,4)
>>> b=(1,2,3,4)
>>> a is b
False
>>> a=c
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a=c
NameError: name 'c' is not defined
>>> c=a
>>> a==c
True
>>> a is c
True
>>> id(a)
1531517845264
>>> id(c)
1531517845264
>>> a is not b
True
>>> a is not c
False
>>> a=10
>>> b=20
>>> a&b
0
>>> a|b
30
>>> a^b
30
>>> a~b
SyntaxError: invalid syntax
>>> a>>b
0
>>> a<<b
10485760
>>> ~a
-11
>>> ~b
-21
