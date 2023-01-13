MIN_DRIVING_AGE = 18

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

def allowed_driving(name, age):

    
    if age >= MIN_DRIVING_AGE:
        f"{name}, is allowed to drive"
    else:
        f"{name}, is not allowed to drive"
    pass


allowed_driving(name, age)