class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        

Bosco = Dog("Golden Retriever", "yellow")
Sage = Dog("German Shepherd", "Brown and white")
print("Bosco is a {} and has a {} coloured fur!".format(Bosco.breed, Bosco.color))
print("Sage is a {} and has a {} coloured fur!".format(Sage.breed, Sage.color))