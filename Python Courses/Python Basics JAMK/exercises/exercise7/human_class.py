class Human:
    def __init__(self, name = "", age = ""):
        self.name = name
        self.age = age

    # override conversion from Human to string
    def __str__(self):
        return "Name: " + self.name + ", " + "Age: " + self.age