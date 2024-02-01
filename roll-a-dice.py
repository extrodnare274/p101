import random

response = "y"

while response.lower() == "y":

    dice_value = random.randint(1,6)

    if dice_value == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")
    elif dice_value ==2:
        print("----------")
        print("| 0      |")
        print("|        |")
        print("|      0 |")
        print("----------")
    elif dice_value ==3:
        print("----------")
        print("| 0      |")
        print("|   0    |")
        print("|      0 |")
        print("----------")
    elif dice_value ==4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")
    elif dice_value ==5:
        print("----------")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")
    elif dice_value ==6:
        print("----------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")

    response = input("Do you want to roll dice again(y/n)?")

print("have a nice day.")