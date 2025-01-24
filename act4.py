#raised exception

try:
    age=int(input("Enter a age: "))
    if age<18:
        raise ValueError
    else:
        print("Valid age")
except ValueError:
    print("Invalid age")