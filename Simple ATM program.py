#1. Prompt user for a pin code
#2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
#You can give a user a maximum of 3 attempts and then exit a program.
#3. Set account balance to 100.
#4. Now we need to simulate cash withdrawal
#5. Accept the withdrawal amount
#6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance
#cannot be negative!)
#7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program

for atm in range(3):
    pin = int(input('Welcome! Please enter your 4-digit pin code: '))
    if pin < 1000 or pin > 9999:
        print("Invalid pin code")
    else:
        print("Pin code entry successful")
        break

#another attempt- attempting to find issue
#counter = 0
#pin_code = int(input("Welcome! Please enter your 4-digit pin code: "))
#while pin_code < 1000 or pin_code > 9999 and counter <= 2:
    #print('Invalid pin code')
    #pin_code = int(input('Re-enter pin code: '))
    #counter = counter + 1
#if counter < 2:
    #print('Pin code successful')
#else:
    #print('Error: three unsuccessful attempts')
    #exit()

account_balance = 100

withdrawal = float(input("Please input the amount you would like to withdraw: £"))
#try:
    #withdrawal = int(input("Input the amount you want to withdraw: £ "))
    #if withdrawal < 0:
        #raise ValueError ('Please enter a positive integer')
#except ValueError as VE:
        #print (VE)

check= input('Please confirm you would like to withdraw £{}: Y or N '.format(withdrawal))
if check.upper() == 'Y':
    print('Transaction in process')
else:
    exit()

try:
    if withdrawal < account_balance:
        remaining= 100 - withdrawal
        print('Successful withdrawal. You have £{} remaining'.format(remaining))
    else:
        print('Error: transaction unsuccessful. Withdrawal amount larger than balance')
finally:
    print('Thank you for using this ATM')



