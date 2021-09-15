from class_car import Car

car_1 = Car("Tesla", "Black", "2021", "120000 $")
car_2 = Car("Lada","White", "2010", "2000 $")
car_3 = Car("Volvo","Black", "2016", "12000 $")

print("-------------------------------------")
car_1.characters()
print("Number of wheels: ", car_1.wheels)
print("-------------------------------------")
car_2.characters()
print("Number of wheels: ", car_2.wheels)
print("-------------------------------------")
car_3.characters()
print("Number of wheels: ", car_3.wheels)
print("-------------------------------------")



def repit(ans):
    ans = ans.upper()
    while ans != "YES" and ans != "NO":
        ans = input(quest_link)
        ans = ans.upper()
    return ans
quest_link = "Show dealers link? (Yes or No): "
answer = repit(input("Show dealers link? (Yes or No): "))

def car_link():
    if answer == "YES":
        quest = input("Write brand of car: ")
        quest = quest.lower()
        quest_link = "Show dealers link? (Yes or No): "
        answer_link = repit(input("Show dealers link? (Yes or No): "))
        if answer_link == "YES":
            print("https://www."+ str(quest) + ".com")
        elif answer_link != "YES":
            print("Good luck!")
    else:
        print("Good luck!")
    quest_link = "How others? (Yes or No): "
    answer_link = repit(input("Show others? (Yes or No): "))
    if answer_link == "YES":
        car_link()
    elif answer_link != "YES":
        print("Good luck!")

car_link()