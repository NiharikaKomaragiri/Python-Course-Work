#Lambda Function

add=lambda a,b:a+b
print(add(9,6))

pow=lambda base,power:base**power
print(pow(7,9))


wish=lambda name: f'{name}, welcome to the class'
print(wish('niharika'))
print(wish('lohisree'))

check=lambda num: 'Even' if num%2==0 else 'odd'
print(check(5))
print(check(10))

squ=lambda num:num**2
print(squ(13))

check=lambda a,b:max(a,b)
print((check(19,20)))

check=lambda s:len(s)
print(check('niharika'))


check=lambda s: 'starts with vowel' if s[0] in 'aeiouAEIOU' else 'not starts with vowel'
print(check('niharika'))
print(check('illusion'))

check=lambda s: 'starts with vowel' if s[0] in 'aeiouAEIOU' else 'not starts with vowel'
s=input()
print(check(s))


check=lambda email: email.split('@') [-1]
email=input()
print(check(email))


check=lambda year: 'leap year' if year%400==0 or(year%4==0 and year%100!=0) else 'not leap year'
year=int(input())
print(check(year))


check= lambda num: num%10
print(check(2024))


l=[1,2,3,45]
res=list(map(lambda i:i**2,l))
print(res)


l=['hello','hi','welcome']
res=list(map(lambda i:i.upper(),l))
print(res)


l={'niha':10,'lohi':90,'ajay':30}
res=dict(sorted(l.items(),key=lambda i:i[1] ))
print(res)
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))


l=[45,6,7,89,34,24,12,2,8]
res = list(filter(lambda i:i%2!=0,l))
print(res)

l='python programming language'
res = list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)


l=['operates','condition','oops','files','exceptions','arthemetic']
res = list(filter(lambda i:i[0] not in 'aeiouAEIOU',l))
print(res)


data={'dell':{'stock':0,'price':83456},
      'lenova':{'stock':15,'price':56900},
      'mac':{'stock':12,'price':90000},
      'hp':{'stock':0,'price':45000}}
res = list(filter(lambda i: data[i]['stock']!=0,data))
print(res)



data={'dell':{'stock':0,'price':83456},
      'lenova':{'stock':15,'price':56900},
      'mac':{'stock':12,'price':90000},
      'hp':{'stock':0,'price':45000}}
res= {i:data[i]['price'] for i in data}
print(res)

low=dict(sorted(res.items(),key=lambda i:i[1]))
print(low)

high=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))
print(high)

#Reduce
from functools import reduce

l=[45,6,7,89,34,24,12,2,8]
s=['operates','condition','oops','files','exceptions','arthemetic']

ms=reduce(lambda sum,i:sum+','+i,s)
ls=reduce(lambda sum,i:sum+i,l)
lm=reduce(lambda prod,i:prod*i,l)

print(ms,ls,lm)


#yield
def reels():
    yield '1-10 files'
    yield '20-30 files'
    yield '30-40 files'
    yield '40-50 files'
    yield '50-60 files'
    yield '60-70 files'
    
        
scroll=reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))













































