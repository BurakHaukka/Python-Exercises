# emf : emission factor
# cons : fuel consumption of the car L/100km
# dist : distance of the trip

def trip_emission(dist, cons, emf):
    emission = dist * (cons/100) * emf/1000
    return print("%.1f" % emission , "kg of CO2")
    