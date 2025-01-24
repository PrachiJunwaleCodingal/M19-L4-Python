#ACP- Age Counter

def age(a):
    try:
        a = int(a)
        if a < 0:
            raise ValueError("Negative number not allowed")
        if a % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")
    
    except ValueError as e:
        print("Invalid age ")

i = input("Enter age: ")
age(i)