#LCM

def LCM(a, b):
    try:
        gr = max(a, b)
        sm = min(a, b)
        for i in range(gr, a*b+1, gr):
            if i % sm == 0:
                return i
    except ValueError as e:
        print("error occured",e)


a = int(input("Enter number1-"))
b = int(input("Enter number2-"))
print("LCM:", LCM(a, b))