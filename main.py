name = input("Type in your name to get started: ")
print("Welcome to my Adventure game,", name + ".")

play = input("You are on an unknown road. You can go left or right to find a route. Which way would you go? (Type right/left or Q to quit): ").lower()

if play == "q":
    quit()

if play == "left":
    play = input("You've come to a river, will you love to walk around or swim? (Type walk/swim): ").lower()

    if play == "walk":
        print(name, "You walked several miles and now out of water. You lost the game!")
    elif answer == "swim":
        print(name, "You swam across the river and got eaten by a crocodile. You lost the game!")
    else:
        print("Not a valid option")
elif play == "right":
    play = input("You've come to an island. Will you call for help or live there forever? (Type call/stay): ").lower()

    if play == "call":
        print("Call dialing...")
        play = input("You called and a stranger picked it. Will you reply or ignore? (Type reply/ignore): ").lower()

        if play == "ignore":
            print("You ignored the stranger, and he got angry. You lost the game!")
        elif play == "reply":
            print("You replied the stranger, and you got saved. You won the game!")
        else:
            print("Not a valid response")
    elif play == "stay":
        print()
    else:
        print("Not a valid option")
else:
    print("Please enter a valid option")