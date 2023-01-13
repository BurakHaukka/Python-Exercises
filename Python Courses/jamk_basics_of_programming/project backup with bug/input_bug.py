from co2 import CO2
from trip_emission_function import trip_emission

#username = os.getlogin()    # Fetch username
#file = open(f'C:\\Users\\{username}\\Desktop\\carbon_emission.txt','w')
#file = open('C:\\Users\\olurt\\Desktop\\carbon_emission.txt','w')

emf_diesel = float(2640) # Diesel CO2 g/liter
emf_petrol = float(2392) # Petrol CO2 g/liter
# Ask user if th1ey want to calculate CO2 emission for how many trips or cars 

option = int(input(""" * You need to know your vehicle's or multiple vehicles' fuel consumption/km to estimate CO2 emission * \n\n
                   Please choose one of the options and enter the number in parenthesis : \n\n\n
                   Calculate CO2 emission for a trip (1) \n
                   !! The results will be saved on Desktop in file Co2_report folder as report.txt !!
                   Calculate and record emissions for multiple cars (2) \n\n
                   Enter your selection: """))

if option == 1 :
   fuel_type = int(input(" What type of fuel ? \n"
                 " Diesel (1) \n"
                 " Petrol (2) \n"
                 "Enter your selection : "))
   if fuel_type == 1 :
      emf = emf_diesel # from gram to kg conversion Diesel CO2 kg/liter   # Floats and integers might cause an issue, keep in mind.
   else:
      emf = emf_petrol # from gram to kg conversion Petrol CO2 kg/liter
   dist = int(input("What is the distance traveled in km ? : "))    # Consider exceptions here !
   cons = int(input("What is average fuel consumption liters/100km ? : "))
   trip_emission(dist, cons, emf)

if option == 2 :
      car_count = int(input("How many cars would you like to record ? (max. 3): "))
      car_list = [] 
      for i in range(car_count):
         car_list.append(CO2())
         car_list[i].car()
      print("Please check the output file on Desktop CO2_report")

