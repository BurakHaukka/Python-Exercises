# I put this together from different searches and this one works as it should, at least in my experience
# When I use a string it says " need integer" also using "0" as input trigger "need integer", when I use 0 it says True, any other number is False.


def isthiszero(num):
   try:
      if not type(num) is int:
         raise TypeError()      
      while num == 0:
         return print("True")
      else:
         print("False")
   except TypeError:
      print("need integer")


# Define a value which is number or string (example: "a" or "4") to num

num = "a"
isthiszero(num)
