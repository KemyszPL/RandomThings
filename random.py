import random


print("Welcome to Random Stuff™️!")
print("Version BETA 8")
print("")
print("Currently avilable Random Stuff™️:")
print("1. Gay Rating")
print("2. 8ball")
print("3. Flip a coin")
print("4. Random insult (very work in progress)")
print("5. Ask Trump")

#the lists
ball8 = ['Yes', 'No', 'Hell naw', 'Doubtful...', 'Sure', 'Absolutely', 'You already know the answer to that...', 'I don`t know, m8', 'Yes, definitely! :D', 'YES YES YES!', 'Nope', 'Most likely!', 'In your dreams!', 'If that`s what you want...', 'Oh God, no.'] #ball8 since i don't think python likes numbers at the begginning of names
asktrump = ['PRESIDENT', 'MELANIA', 'OIL', 'MIKE PENCE', 'BUSH', 'PEDOPHILE', 'HOMOSEXUAL', 'REAL', 'IRAN','THE BEST', 'AFGHANISTAN', 'MESS', 'FAKE MEDIA', 'PUTIN', 'ALIENS', 'RIGGED', 'DOING POORLY']

usrinput = input("? ")

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
    output = str(random.choice(ball8)) #NEW: Code was optimized a lot!
    print(output)
#Flipping a coin
if usrinput == "3":
    num = str(random.randint(1,2))
    if num == "1":
        print("threw a coin: tails!")
    elif num == "2":
        print("threw a coin: heads!")
#Random insult
if usrinput == "4": #remind me to finish this
    num = str(random.randint(1,2))
#Ask Trump
if usrinput == "5":
    usrinput = input("What do you want to ask Trump? ")
    output1 = "You: " + usrinput
    output2 = "Trump: " + random.choice(asktrump)
    print(output1)
    print("")
    print("")
    print(output2)
