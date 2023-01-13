# Make a program that asks the user for 3 integers and prints the largest of them.

int1 = int(input("Input first integer: "))

int2 = int(input("Input second integer: "))

int3 = int(input("Input third integer: "))

if int1 > int2 and int1 > int3:
    print(int1)
    
elif int2 > int1 and int2 > int3:
    print(int2)

elif int3 > int1 and int3 > int2:
    print(int3)
