def show_info():
    print("I am Utils.Info")
    
def substract():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))    
    sub = num1 - num2
    print(sub)
    
def average():
    numav1 = int(input("Please enter first number: "))
    numav2 = int(input("Please enter second number: "))
    numav3 = int(input("Please enter third number: "))
    av = (numav1 + numav2+ numav3)/3
    print("Average is ", "%.1f" % av)
    
def calc_consumption(consum, fprice, dist):
        fuel_cons = (consum * dist) / 100
        cost = fprice * fuel_cons
        print("Consumption is ", "%.1f" % fuel_cons, "liters", "and cost is ", "%.1f" % cost,"Euros")