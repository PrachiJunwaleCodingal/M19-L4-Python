#bye bye- will gets printed for all even numbers

valid = False

while not valid:
  try:
    n = int(input("Enter number: "))
    while n % 2 == 0:
      print("bye bye")
      valid = True

  except ValueError:
    print("Invalid:its not number")