import random


print("Welcome to Random Stuff™️!")
print("Version BETA 14")
print("")
print("Currently avilable Random Stuff™️:")
print("1. Gay Rating")
print("2. 8ball")
print("3. Flip a coin")
print("4. Random insult")
print("5. Ask Trump")
print("6. Kill (WIP)")

#the lists
ball8 = ['Yes', 'No', 'Hell naw', 'Doubtful...', 'Sure', 'Absolutely', 'You already know the answer to that...', 'I don`t know, m8', 'Yes, definitely! :D', 'YES YES YES!', 'Nope', 'Most likely!', 'In your dreams!', 'If that`s what you want...', 'Oh God, no.'] #ball8 since i don't think python likes numbers at the begginning of names
asktrump = ['PRESIDENT', 'MELANIA', 'OIL', 'MIKE PENCE', 'BUSH', 'PEDOPHILE', 'HOMOSEXUAL', 'REAL', 'IRAN','THE BEST', 'AFGHANISTAN', 'MESS', 'FAKE MEDIA', 'PUTIN', 'ALIENS', 'RIGGED', 'DOING POORLY']
insults = ['I don`t exactly hate you, but if you were on fire and I had water, I`d drink it.', ', I tried to see things from your perspective, but I couldn`t seem to shove my head that far up my ass.', ', I wasn`t born with enough middle fingers to let you know how I feel about you.', 'Hey, your village called – they want their idiot back.', 'It`s kinda sad watching you attempt to fit your entire vocabulary into a sentence.', 'You`re so fat when you go on an airplane, you have to pay baggage fees for your ass.', 'I`m not saying I hate you, but I would unplug your life support to charge my phone.', 'You`re so fat when you go swimming the whales start singing "We Are Family".', 'That little voice in the back of your head, telling you you`ll never be good enough? It`s right.', 'You bring everyone a lot of joy, when you leave the room.', 'If I ate a bowl of alphabet soup, I could shit out a smarter sentence than any of yours.', 'I would agree with you but then we would both be wrong.', 'You`re so fat that when you farted you started global warming.', 'What`s the difference between you and Hitler? Hitler knew when to kill himself.', 'Why is it acceptable for you to be an idiot but not for me to point it out?', 'I`m sorry I didn`t get that - I don`t speak idiot.', 'Yo mamma is so ugly her portraits hang themselves.', 'You`re so ugly that even Scooby Doo couldn`t solve that mystery.', 'Looks like you fell off the ugly tree and hit every branch on the way down.', 'I thought of you today. It reminded me to take the garbage out.', 'Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.', 'Your birth certificate is an apology letter from the condom factory.', 'Don`t feel sad, don`t feel blue, Frankenstein was ugly too.', 'If you spoke your mind, you`d be speechless.', 'I fart to make you smell better.', 'You`re so fat you jumped off the Grand Canyon and got stuck.', 'You`re so fat when you stepped on the scale, Buzz Lightyear popped out and said "To infinity and beyond!"', 'You`re so fat you need cheat codes to play Wii Fit', 'Dumbass.', 'You`re so fat you`d have to go to Sea World to get baptized.', 'You`re so fat I could slap your butt and ride the waves.', 'Ordinarily people live and learn. You just live.', 'If ignorance is bliss, you must be the happiest person on earth.', 'You`re the reason the gene pool needs a lifeguard.', 'It looks like your face caught on fire and someone tried to put it out with a hammer.'] #wow this is LONG (i swear if i have to change them in the future i'll just throw it in the garbage)
kills = ['Aids, KILLNAME died from aids.', 'KILLNAME was being KILLNAME.']

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
if usrinput == "4":
    insult = str(random.choice(insults))
    name = input("Who do you want to insult? ")
    print(name + ", " + insult)
#Ask Trump
if usrinput == "5":
    usrinput = input("What do you want to ask Trump? ")
    output1 = "You: " + usrinput
    output2 = "Trump: " + random.choice(asktrump)
    print(output1)
    print("")
    print("")
    print(output2)
#Kill
if usrinput == "6":
    name = input("Who do you want to kill? ")
    kill = random.choice(kills)
    if "KILLNAME" in kill:
        print(kill.replace('KILLNAME', name))
    else:
        print(name + " " + kill)
