# Make a program that asks the user his/her age.
# if the age is less than 13 years, print "child"
# if the age is 13-19 years, print "teen"
# if it is 20-65 years old, print "adult"
# otherwise print "senior". #

age = int(input("How old are you?: "))

if age <= 13:
    print("Child")
    
elif 13 < age <= 19:
    print("Teen")
    
elif 20 <= age <= 65:
    print("Adult")

else:
    print("Senior")
