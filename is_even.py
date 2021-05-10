#Returns True if the number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

myNumber = is_even(44)
print(myNumber)

#Returns true if the number is odd
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

myOddNumber = is_odd(43)
print(myOddNumber)



