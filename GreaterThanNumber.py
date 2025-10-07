menu = True
while menu:
  user_choice = 0
  user_choice = int(input("If you want to identify the smallest value, pick 1. If you want to identify the largest value, pick 2. To quit, pick 3: "))
  
  #1:To find small number
  if user_choice == 1:
    small = 0
    small = int(input("Pick any small value you could think of (To quit, type -1000): "))
    if small != -1000:
      print(small, "is the small value.")
      smaller = 0
      while smaller != -1000:
        smaller = int(input("Let's pick another value that could be smaller than the current value: "))
        if smaller == -1000:
          continue
        elif small > smaller:
          print(smaller, "is your small value.")
        elif small < smaller:
          print(smaller, "is still bigger than the current value.")
      else: 
        continue

  #2:To find large number
  elif user_choice == 2:
    large = 0
    large = int(input("Pick any large value you could think of (To quit, type -1000): "))
    if large != -1000:
      print(large, "is the big current value.")
      bigger = 0
      while bigger != -1000:
        bigger = int(input("Let's pick another value that could be bigger than the current value (To quit, type -1000): "))
        if bigger == -1000:
          continue
        elif large > bigger:
          print(large, "is still your large value.")
        elif large < bigger:
          print(bigger, "is the larger value.")
      else: 
        continue

  #3: Quit
  else:
    print("Come back soon!")
    break