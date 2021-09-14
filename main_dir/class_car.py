class Car:

    def __init__(self, model,color,year):
        self.model = model
        self.color = color
        self.year = year

    def characters(self):
        print("This car is " + self.model + "!")