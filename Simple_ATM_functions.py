#smaller functions to test

#checks for a valid pin that is 4 digits
def pin(num):
    valid_pin = range(1000, 9999)
    if num in valid_pin:
        return True
    else:
        return False

print(pin(209))

#checks given pin is an integer
def check_int(num1):
    if num1 is not int:
        raise TypeError('Please enter integers')

check_int('abc')

#checks withdrawal amount is positive
def check_pos(num2):
    if num2 < 0:
        raise ValueError('Please enter a positive number')

check_pos(-19)

#checks balance amount is positive
def check_remaining(num4):
    if num4 > 0:
        return True
    else:
        return False

check_remaining(-19)

#checks withdrawal calculation
def check_withdraw(num3):
    return 100 - num3
print(check_withdraw(30))