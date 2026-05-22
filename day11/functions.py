#Functions

def greet(name):
    print(f'Hello {name}, welcome to the python')
name=input()
greet(name)

def alert(msg):
    print(f'Memory is full {msg},need to free space')
alert('in Gmail')

def display(name,phoneNo,email):
    print(f'Enter your name: {name}')
    print(f'Enter your number: {phoneNo}')
    print(f'Enter the email: {email}')
    
name=input('Enter the name:')
phoneNo=int(input('Enter the PhoneNo'))
email=input('Enter the email')
display(name,phoneNo,email)


def display(name,email,phoneno=None,cgpa=None):
    print(f'name: {name}')
    print(f'phoneno {phoneno}')
    print(f'Email {email}')
    print(f'cgpa {cgpa}')

display('niharika','szdxfcg@gmail.com','34345678',8.5)
display('niharika','szdxfcg@gmail.com')

def display(*names):
    print(names)

display('niharika')
display('lohi','navi')
display('vijay','nivitha','kumar','sree')

#output will be tuple

def display(**names):
    print(names)

display(n='niharika')
display(k='lohi',l='navi')
display(m='vijay',y='nivitha',o='kumar',s='sree')
#output will be dictonary

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
    
print("prime number"if prime(n) else "not a prime number")




















