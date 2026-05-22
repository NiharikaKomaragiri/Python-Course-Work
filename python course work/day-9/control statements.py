'''
Control statements
1.iterative
for loop while loop
for=will print until the condition is false
while=will print after the condidtion false for 1 time

for var in seq:
-> str,list,tuple,set,dict,range()

for var in enumerate(seq):

for car in range(start,stop+1,step)

pass is for the pass the statement or empty block code
'''
pin=1234
for i in range(5):
    entered_pin=int(input("Enter the pin:"))
    if entered_pin==pin:
        print("unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("try after sometime")
    
