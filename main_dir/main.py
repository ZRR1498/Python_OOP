from class_car import Car

car_1 = Car("Tesla", "Black", "2021", "120000 $")
car_2 = Car("Lada","White", "2010", "2000 $")
car_3 = Car("Volvo","Black", "2016", "12000 $")

print()
car_1.characters()
print("Number of wheels: ", car_1.wheels)
print("-------------------------")
car_2.characters()
print("Number of wheels: ", car_2.wheels)

def repit():
    answer = 0
    while answer != "YES" or "NO":
        answer = input("Show dealers link? (Yes or No): ")
        answer = answer.upper()
        if answer == "YES" or "NO":
            return answer

answer = repit()
if answer == "YES" or "NO":
    if answer == "YES":
        quest = input("Write brand of car: ")
        quest = quest.lower()
        answer = input("Show dealers link? (Yes or No): ")
        on_display = ("https://www."+ str(quest) + ".com")

    elif answer == "NO":
        print("Good luck!")