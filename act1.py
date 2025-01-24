#valueError

try : 
  num = int(input("Enter number : "))
  print(num)
except ValueError as e:
  print("Exception: ",e)


print("Out of exception")