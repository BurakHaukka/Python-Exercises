import random

x = int(input("How many sets of lottery numbers you want?: "))

def lottery(x):
      for x in range(x):
            lottery_numbers = random.sample(range(1,41), 7) # random.sample() function supposed to selects unique elements
            lottery_numbers = sorted(lottery_numbers)
            print(lottery_numbers)
  
lottery(x)