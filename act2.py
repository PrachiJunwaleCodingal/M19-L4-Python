#multiple exceptional
try:
  n1 = int(input("Enter a number: "))
  n2 = int(input("Enter a number: "))
  result = n1/n2
  print("Result : ", result)
  print("Result : ", result1)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numbers only")
except NameError as e:
     print("Exception is ",e)
except:
     print("Some other error")
finally:
     print("Finally executed")