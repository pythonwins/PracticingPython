def get_num():
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")
        
    if num % 4 == 0:
        print("This number is a multiple of 4.")
    else:
        print("This number is not a multiple of 4.")
        
    return num

def next_num():
    num0 = int(input("Please enter a number: "))
    num1 = int(input("Please enter another number: "))
    check = num0 / num1
    if num0 % num1 == 0:
        print("%s , these numbers divide evenly." % check)
    else:
        print("%s , these numbers do not divide evenly." % check)

get_num()
next_num()
