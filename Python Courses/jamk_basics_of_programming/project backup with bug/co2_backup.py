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

emf_diesel = float(2640/1000)
emf_petrol = float(2392/1000)


class CO2:
    def __init__(self, brand = "", model = "", fueltype = 0, fuelname = "", dist = 0, cons = 0, emission = 0):
        self.brand = brand
        self.model = model
        self.fueltype = fueltype
        self.fuelname = fuelname
        self.dist = dist
        self.cons = cons
        self.emission = emission
    @classmethod
    def car(self):
        while 1: ##### Same as while True
            try:
                brand = input("Enter brand of the car: ")
                print("\n"*3)
                model = input("Enter model of the car: ")
                print("\n"*3)
                
                dist = int(input("Enter distance traveled in km : "))
                print("\n"*3)
                cons = int(input("Enter fuel consumption of the trip in L/100km : "))
                print("\n"*2)
                emission = 0
                fueltype = int(input("Enter fuel type of the car diesel (1) or petrol (2) : "))
                if fueltype == 1:
                    fuelname = "Diesel"
                    emission = dist * (cons/100) * emf_diesel
                if fueltype == 2:
                    fuelname = "Petrol"
                    emission = dist * (cons/100) * emf_petrol
                print("\n"*3)                
                return self(brand, model, fueltype, fuelname, dist, cons, emission)
            except:
                print('Invalid input!')
                continue   
    def car_info(self):
        return "Brand : " + self.brand + "\nModel : " + self.model + "\nFuel type : " + self.fuelname + "\nTravel Distance : " + str(self.dist) + " km \nAvg. Consumption : " + str(self.cons) + " liter/km." + "\nCO2 emitted : " + str(self.emission) + "kg"  
            
    brand = ""
    model = ""
    fueltype = ""
    fuelname = ""
    dist = ""
    cons = ""
    emission = ""

    
    