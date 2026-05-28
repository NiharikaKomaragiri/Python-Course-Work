'''
ATM Application

verifypin
check balance
deposit
withdraw
transactions

'''
#data from bank
data={
    5678923:{'pin':2345,'balance':5000,'Username':'niharika','history':[]},
    5672022:{'pin':2322,'balance':15000,'Username':'lohisree','history':[]},
    56782023:{'pin':3456,'balance':10000,'Username':'vijay','history':[]},
    56720243:{'pin':6789,'balance':45000,'Username':'nivitha','history':[]}
     }

#To login into account
def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin']==pin:
        print('login succesful')
        return True
    else:
        print('login failed. Try Again!!!')
        return False

#Options
def options():
    print()
    print('[D]eposite')
    print('[W]ithdraw')
    print('[C]heck Balance')
    print('[V]iew Transactions')
    print('[E]xit')

#To deposit money
def deposit():
    amount=int(input("Enter the amount:"))
    data[acc_num]['balance'] += amount 
    print(f'{amount} is deposited succesfully')
    data[acc_num]['history'].append(f"{amount} is deposited")

#To withdraw money
def withdraw():
    amount=int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        
        data[acc_num]['balance'] -= amount
        print(f'{amount} is withdraw succesfully')
        data[acc_num]['history'].append(f"{amount} is withdraw")
    else:
        print('Insufficient amount')

#To check the balance
def checkBalance():
    balance = data[acc_num]['balance']
    print(f"Current Balance{balance}")

#To view Transactions history
def viewTransactions():
    if data[acc_num]['history']:
        print(f"-----Transaction History------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("------End Of Transactions-----")
    else:
        print("No Transactions")
