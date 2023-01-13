# Error message is 'builtins.IndexError: list assignment index out of range'

try:
    list = [1, 2, 3, 4,]
    list[4] = (5) # using index 5 triggers exception
except IndexError:
    print("List doest not have that index !")
    

