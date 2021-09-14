class Car:
    wheels = 4
    def __init__(self, model,color,year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def characters(self):
        print("Brand: " + self.model)
        print("Color: " + self.color)
        print("Year: " + self.year)
        print("The cost of this car: " + self.price)

