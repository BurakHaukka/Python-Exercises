class Car:
    
    def __init__(self, brand = "", model = "", price = ""):
        self.brand = brand
        self.model = model
        self.price = price
             
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)
           
    brand = ""
    model = ""
    price = ""
    