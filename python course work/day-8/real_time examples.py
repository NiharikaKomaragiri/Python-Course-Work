'''
1.mobile battery,discount
2.login,otp
3.movie ticket booking,order fare
4.order proc

ch=int(input("Enter the battery per:"))
if ch<=20:
    print("Battery is low")


discount=int(input("Enter the discount:"))
price=int(input("Enter the price:"))
if discount:
    price -= price*(discount/100)
    print("discount applied")
print("price:",price)

#Original Price = ₹1000
Discount = 20%

👉 Discount = (20 × 1000) / 100 = ₹200
👉 Final Price = 1000 − 200 = ₹800

dict={ "Niharika":"niha2004",
       "Lohisree":"lohi2012",
       "vijaykumar":"vijay2004"}
username=input("Enter the username:")
password=input("Enter the password:")
if dict.get(username)==password:
    print("Login successful")
else:
    print("Login Failed")

#OTP verification
import random
otp=random.randint(0000,9999)
print("your otp:",otp)
entered_otp=int(input("Enter the OTP:"))
if otp == entered_otp:
    print("verified successfully")
else:
    print("Invalid OTP")

hr,min=list(map(int,input("Enter the time (HH:MM):").split(':')))
fare=0
price=350
if 0<=hr<=23 and 0<=min<=59:
    if 8<=hr<=16:
        fare=40
    elif 17<=hr<=23:
        fare=100
    elif 0<=hr<=7:
        fare=150
    print("Total Fare:",fare+price)
else:
    print("Invalid time")
'''
data={
    'niharika':{'status':True,'python':70,'mysql':80,'flask':60},
    'lohisree':{'status':True,'python':77,'mysql':90,'flask':90},
    'vijaykumar':{'status':True,'python':80,'mysql':70,'flask':90},
    'nivi':{'status':True,'python':67,'mysql':78,'flask':78},
    'nivitha':{'status':False,'python':None,'mysql':None,'flask':None},
    'vinika':{'status':True,'python':60,'mysql':80,'flask':88},
    }
name = input("Enter the student name: ")
if name in data:
    print(name,"'s Report:")
    if data[name]['status']:
        avg = (data[name]['python']+data[name]['mysql']+data[name]['flask'])/3
        if avg>80:
            print('Congrations, Well Done')
        elif avg>60:
            print('Good, Improvement needed')
        elif avg>35:
            print('Just Passed, Better luck next time')
        else:
            print("Failed in the exam. Please bring your parents")
    else:
        print("Didn't attempt the exam.")
else:
    print(name,"'s data is not found")


    









































