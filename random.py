import random


print("Welcome to Random Stuff™️!")
print("Version BETA 6 hotfix")
print("")
print("Currently avilable Random Stuff™️:")
print("1. Gay Rating")
print("2. 8ball")
print("3. Flip a coin")

usrinput = input("? ")
while True:
    #Gay Rating
    if usrinput == "1":
        usrinput = input("What do you want to rate? ")
        num = str(random.randint(1,2)) #Two levels for more randomization
        if num == "2": #Reversed for higher results because the rng does not like to rng
            num = str(random.randint(1,50))
            out = (usrinput + " is " + num + "% gay")
            print(out)
        elif num == "1":
            num = str(random.randint(50,100))
            out = (usrinput + " is " + num + "% gay")
            print(out)
    #8ball
    if usrinput == "2":
        usrinput = input("What do you want to ask? ")
        num = str(random.randint(1,15))
        if num == "1": #Randomizing the answer
            print("Yes")
        elif num == "2":
            print("No")
        elif num == "3":
            print("Hell naw")
        elif num == "4":
            print("Doubtful...")
        elif num == "5":
            print("Sure")
        elif num == "6":
            print("Absolutely")
        elif num == "7":
            print("You already know the answer to that...")
        elif num == "8":
            print("I don't know, m8")
        elif num == "9":
            print("Yes, definitely! :D")
        elif num == "10":
            print("YES YES YES!")
        elif num == "11":
            print("Nope")
        elif num == "12":
            print("Most likely!")
        elif num == "13":
            print("In your dreams!")
        elif num == "14":
            print("If that's what you want...")
        elif num == "15":
            print("Oh God, no.")
    #Flipping a coin
    if usrinput == "3":
        num = str(random.randint(1,2))
        if num == "1":
            print("threw a coin: tails!")
        elif num == "2":
            print("threw a coin: heads!")
