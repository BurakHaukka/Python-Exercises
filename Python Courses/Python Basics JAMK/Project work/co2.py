# Carbon emission of a car can be estimated by distance travelled, fuel consumption and emission factor. 
# Source: https://www.ibm.com/docs/en/tririga/10.8?topic=SSFCZ3_10.8/com.ibm.tri.doc/tre_measure/r_carbon_fp_calc.html
# This calculation kind of makes sense, but I could not be sure. 

# Estimated emission factors are different for different fuels. Emission factors are taken from an online source for easier estimation.
# There is more information how they are calculated on the source page.
# Source: https://ecoscore.be/en/info/ecoscore/co2

# emf : emission factor
# cons : fuel consumption fo the car
# dist : distance of the trip
# emis : Total CO2 emission of the travel

import os.path



emf_diesel = float(2640/1000)
emf_petrol = float(2392/1000)


class CO2:
    @classmethod
    def car(cls):
        output = []
        try:
            filename = "report.txt"
            path = os.path.expanduser("~/Desktop/CO2_report") # I wanted to save on the desktop.
            if not os.path.exists(path): os.makedirs(path)
            path += "/"
            file = open(path + filename, "a+")
        except:
            print("Failed to create")                
        try:
            cls.brand = input("Enter brand of the car: ")
            output.append(" Brand: " + cls.brand)
            print("\n"*3)
            cls.model = input("Enter model of the car: ")
            output.append(" Model: " + cls.model)
            print("\n"*3)
            cls.dist = input("Enter distance traveled in km : ")
            output.append(" Distance: " + cls.dist + "km")
            print("\n"*3)
            cls.cons = input("Enter fuel consumption of the trip in L/100km : ")
            output.append(" Consumption: " + cls.cons + "L/100")
            print("\n"*2)
            cls.emission = 0
            fueltype = int(input("Enter fuel type of the car diesel (1) or petrol (2) : "))
            if fueltype == 1:
                cls.fuelname = "Diesel"
                cls.emission = int(cls.dist) * (int(cls.cons)/100) * emf_diesel
                output.append(" Fuel name: " + cls.fuelname)
                output.append(" Emission: " + str("%.1f" % cls.emission) + "kg")
            if fueltype == 2:
                cls.fuelname = "Petrol"
                cls.emission = int(cls.dist) * (int(cls.cons)/100) * emf_petrol
                output.append(" Fuel name: " + cls.fuelname)
                output.append(" Emission: " + str("%.1f" % cls.emission) + "kg")                    
            print("\n"*3)
        except:
            print('Invalid input!')
        file.writelines(','.join(output) + '\n') 
        file.close() 
            
    brand = ""
    model = ""
    fueltype = ""
    fuelname = ""
    dist = ""
    cons = ""
    emission = ""

    
    