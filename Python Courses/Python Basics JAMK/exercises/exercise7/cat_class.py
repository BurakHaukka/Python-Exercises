class Cat:
    def __init__(self, name = "", color = ""):
        self.name = name
        self.color = color


# print conversion for cat
    def __str__(self):
        return self.name + ", " + "Color: " + self.color
    
    def meow(self):
        if self.name == "Katsi":
            return self.name + ": " + "Hisseesss !!"
        else:
                    return self.name + ": " + "Meeooow"
    