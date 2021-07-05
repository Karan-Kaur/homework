# Lesson 8- Simple ATM program which allows for cash withdrawal

#for atm in range(3):
    #pin = int(input('Welcome! Please enter your 4-digit pin code: '))
    #if pin < 1000 or pin > 9999:
        #print("Invalid pin code")
    #else:
        #print("Pin code entry successful")
        #break
def check_balance():
    checking = input('Would you like to check your balance? Y/N ')
    if checking.upper() == 'Y':
        print('Your balance is £100')
        withdraw()
    else:
        withdraw()

def withdraw():
    account_balance = 100
    withdrawal = float(input("Please input the amount you would like to withdraw: £")) #tried to make exception for neg integers but did not work
    check = input('Please confirm you would like to withdraw £{}: Y/N '.format(withdrawal))
    if check.upper() == 'Y':
        print('Transaction in process')
    else:
        exit()
    try:
        if withdrawal < account_balance:
            remaining = 100 - withdrawal
            print('Successful withdrawal. You have £{} remaining'.format(remaining))
        else:
            print('Error: transaction unsuccessful. Withdrawal amount larger than balance')
    finally:
        print('Thank you for using this ATM')
        exit()

import sys
def pin_code():
    counter = 0
    while counter < 3:
        pin = int(input('Welcome! Please Enter Your 4 Digit Pin code:')) #tried to make exception if user inputted strings but did not work
        if pin > 1000 and pin < 9999:
            print("Pin code accepted!")
            check_balance()
            exit()
        else:
            print("Invalid pin")
            counter += 1
    sys.exit("Three unsuccessful attempts. Please exit ")

pin_code()
