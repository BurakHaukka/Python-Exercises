# Using == operator because I assumed there is no decimals involved in grading and there is no range of points (except grade 5 is 10,11,12) #

points = int(input("Please enter points: "))

if points == 0 or points == 1:
    print(0)
    
elif points == 2 or points == 3:
    print(1)
    
elif points == 4 or points == 5:
    print(2)
    
elif points == 6 or points == 7:
    print(3)
    
elif points == 8 or points == 9:
    print(4)
    
elif 10 <= points <= 12:
    print(5)
    
else:
    print("There is no way to have that much points.")