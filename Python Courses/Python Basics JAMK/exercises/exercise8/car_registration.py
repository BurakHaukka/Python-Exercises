car_registration = {
    "SFT-412": "Skoda",
    "HFU-745": "Opel",
    "GHF-784": "Anadol",
    "XVS-512": "Tofas",
    "SFC-963": "VW",
    "HSV-541": "Opel",
    "JGS-538": "Mercedes",
    "JBN-523": "Tesla",
    "LKF-865": "Toyota",
    "KFL-412": "Ford",
}

#print(sorted(car_registration))
#print(sorted(car_registration.values()))

# Sorted by license plate
sorted_reg = dict(sorted(car_registration.items(), key = lambda x: x[0].lower()))

for k, v in sorted_reg.items():
    print('{}: {}'.format(k, v))
    
# Sorted by maker
sorted_reg = dict(sorted(car_registration.items(), key = lambda x: x[1].lower()))

for k, v in sorted_reg.items():
    print('{}: {}'.format(k, v))

