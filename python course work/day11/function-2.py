'''
def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol:
                vc+=1
            else:
                cc+=1
        elif i.isdigit:
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
    print(f"vol count:{vc}")
    print(f"digit count:{dc}")
    print(f"con count:{cc}")
    print(f"word count:{wc}")
    print(f"space count:{sc}")
check('python programming LANGUAGE 255 *&@CODEGAN')

def display():
    num+=10
    print("inside num:",num)
num=10
display()
print('outside num:',num)

def display(n):
    n=[1,2,3,4]
    print("inside num:",num)
n=[10,11,12]
display()
print('outside num:',num)

def display(n):
    n=(1,2,3,4)
    print("inside num:",num)
n=(10,8,9)
display()
print('outside num:',num)

def display(n):
    n=False
    print("inside num:",num)
n=True
display()
print('outside num:',num)

def display(n):
    n=n+'False'
    print("inside num:",num)
n='True'
display()
print('outside num:',num)



def display():
    #keyword global we effect outside of the block 
    global num
    num+=10
    print("inside num:",num)
num=10
display()
print('outside num:',num)

def slot():
    course='java full stack'
    print('slot is booked in JFS',course)

course='python'
slot()
print('slot changed to PFS',course)

#by using def in def
def slot():
    course='java full stack'
    print('slot is booked in JFS',course)
    def change():
        nonlocal course
        course='python'
        print('changed',course)
    change()
    print('final',course)
slot()

def slot():
    course='java full stack'
    print('slot is booked in JFS',course)
    def change():
        global change
        course='python'
        print('changed',course)
    change()
    print('final',course)
slot()

s='python'
len=5
print(len)


#to terminate the block of code in function
def display():
    print('start')
    return
    print('end')
display()

def display(n):
    if n==11:
        return n
    print(n)
    display(n+1)
display(1)


def display(n):
    if n==11:
        return n
    display(n+1)
    print(n)
display(1)


def display(s,ind):
    if ind==len(s):
        return ind
    print(s[ind])
    display(s,ind+1)
    
s='python'
display(s,0)

def display(s,ind):
    if ind==len(s):
        return ind
    
    display(s,ind+1)
    print(s[ind])
    
s='python'
display(s,0)


def display(s,ind):
    if ind==len(s)+1:
        return ind
    
    print(s[: ind])
    display(s,ind+1)
    
    
s='python'
display(s,1)


def display(s,ind,end):
    if ind==len(s)-end+1:
        return 
    
    print(s[ind:ind+end])
    display(s,ind+1,end)
    
    
s='python programming'
display(s,0,4)
'''
def display(s):
    print(s)
display(10)








