
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 # Intro
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest in the forbidden forest!")
import time
print("You find yourself on the edge of the forbidden forest, though it is off limits for students of Hogwarts to go unaccompanied.")
time.sleep(2)
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
        response = input("Would you like to step into the forest?\nyes/no\n")
        if response == "yes":
                print("You head into the forest. You hear centuars galloping in the distance and also a wolf howling. Apparenly there is a rumour that a Werewolf briefly roamed here twenty some years ago. \n")
        elif response == "no":
                print("You are not ready for this quest. Goodbye, " + name + ".")
                time.sleep(2)
                quit()
        else: 
                print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a hippogriff that is charging quickly towards you.")
    print("To your right, there is more forest with no end.")
    print("Hagrid's hut is in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The hipogriff got offended because you didn't bow and wait for it to make the first move, so its talons stabbed you. Farewell," + name + ".")
        time.sleep(2)
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("Are you stupid? Of course, you wouldn't want Hagrid to find out, he is literally a night owl. He's going to find out and notify McGonagall, then your time at Hogwarts is going to be over. Bye then!")
        time.sleep(2)
        quit()
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        time.sleep(2)
        quit()
    else:
        print("I didn't understand that.\n")

def scene2():
    import time
    time.sleep(2)
    print("""
          The moon is glowing, the gold and white fur of the unicorns glimmer. While observing your reflection in a mini riverstream, you see an enchanted rose across from it. People for thousands of year have never attempted to take that rose away from the forbidden rose due to a legend that one who takes it for thyself never leaves the forest for some odd reason.
""")
response = ""
while response not in directions:
    print("To your left, you see a tree with an bowtruckle inhabitating it. You've never seen a bowtruckle before.")
    print("To your right, you hear a distinctive clicking sound.")
    print("The rose is in front of you, only a river apart.")
    print("Behind you is where you were moments before.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("You touched the tree hole, the bowtruckle thought its tree was in danger. So, now you are blind. It's tragic and karma," + name + ".")
        time.sleep(2)
        quit()
    elif response == "right":
        print("You discover that clicking sound came from an Acromantula, a large venomous spider covered in thick black hair. Soon, crowds of Acromantula swarm around you because they think you're a great place for their eggs to hatch. Well, adventurer your journey ends!\n")
        time.sleep(2)
        quit()
    elif response == "forward":
        print("You notice on the ground that there's strands of unicorn tail hair, which you use to tie the fallen branches to make a makeshift boat.")
    elif response == "backward":
        print("You're pathetic, c'mon I thought you were adventurous. Bye, " + name + ".")
        time.sleep(2)
        quit()
    else:
        print("I didn't understand that.\n")

response = ""
while response not in yes_no:
        print("After rowing across the river, you finally get to touch the rose. It's luscious and the colour of a rare shade of red you've never seen before, encompassed a translucent glass. :rose: You decide to shatter the translucent glass and take the rose away with you")
        response = input("Do you want to go back to your Hogwarts dorm?\nyes/no\n")
        if response == "yes":
                print("Great idea! I think the sun is rising after a long beauty sleep, also don't want the house ghosts gossiping. Farewell till next time!\n")
        elif response == "no":
                print("Well, you should cause I can tell see your eyebags from another country, " + name + ".")
                time.sleep(2)
                quit()
        else: 
                print("I didn't understand that.\n")