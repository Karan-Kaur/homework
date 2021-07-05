#ATM functions
#breaking into chunks for unit testing
def pin_code():
    for atm in range(3):
        pin = int(input('Welcome! Please enter your 4-digit pin code: '))
        if pin < 1000 or pin > 9999:
            print("Invalid pin code")
        else:
            print("Pin code entry successful")
            break
pin_code()

def withdraw():
    account_balance = 100
    withdrawal = float(input("Please input the amount you would like to withdraw: £"))
    check = input('Please confirm you would like to withdraw £{}: Y or N '.format(withdrawal))
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

withdraw()


#attempting without user input
def pin_code3(pin_no):
    if pin_no < 1000 or pin_no > 9999:
        return False
    else:
        return True

def pin_code2(pin_no1):
    if pin_no1 < 1000 or pin_no1 > 9999:
        return 'Invalid'
    else:
        return 'Successful'