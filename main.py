name = input("Type in your name to get started: ")
print("Welcome to my Adventure game,", name + ".")

play = input("You are on an unknown road. You can go left or right to find a route. Which way would you go? (Type right/left or Q to quit): ").lower()

if play == "q":
    quit()

if play == "left":
    play = input("You've come to a river, would you love to walk around or swim? (Type walk/swim): ").lower()

    if play == "walk":
        print(name, "You don waka go where you no know o. You lost the game!")
    elif answer == "swim":
        print(name, "You don swim go where you no know sha. You lost the game!")
    else:
        print("Not a valid option")
elif play == "right":
    print()      