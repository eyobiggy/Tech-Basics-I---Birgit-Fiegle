import time

print ("We wish you a very warm welcome at Astarion - the most renowned Academy for Witchcraft in the country!\n")
time.sleep(5)
print ("Here you will have the chance to discover unknown talents and prove yourself worthy to be a part of witchcraft society.\nDo you have the courage and the wit to master this challenge? Let's find out!\n")
time.sleep(8)
print("I am Professor Nutmeg. I will teach you the basics of wizardy and will help you master your first challenges.\n")

time.sleep(5)

print ("Let's begin with your first spell casting lesson.\n")

time.sleep(3)

spell1 = ""

while spell1 not in ["galea"]:
    spell1 = input ("Type 'Galea' in order to produce wind.\n").strip().lower()
    if spell1 not in ["galea"]:
        time.sleep(1)
        print ("Invalid answer. Please type 'Galea' to try out the spell.")


if spell1 == "galea":
    time.sleep(1)
    print ("Do you see the piece of cloth I placed in front of you? Your goal is to get it off the table with your wind spell. \nBut careful: we don't want it flying through the whole room!\n")
    time.sleep(7)

    while True:
        mana1 = input (f"Type in a number between 1 and 10 to choose the appropriate amount of mana.\n").strip()
        if not mana1.isdigit():
            print ("This is not a number, my apprentice.Try again.\n")
            time.sleep(2)
            continue

            # loop created with help of ChatGBT

        mana1 = int(mana1)
        if mana1 > 10 or mana1 < 1:
            print ("Please enter a number between 1 and 10.\n")
            time.sleep(2)
            continue

        elif mana1 > 3 and mana1 <= 5:
            print ("Perfect! Your piece of cloth slides elegantly off the table and lands on the ground a few meters away from you.\n")
            time.sleep(3)
            break

        elif mana1 <= 2 and mana1 >= 1:
            print("That was not strong enough. Try it with a little more force.\n")
            time.sleep(3)
            continue

        else:
            print ("Careful there! That was way too strong. The cloth is flying through the whole room. Try it a little softer.\n")
            time.sleep(3)
            continue

print ("You are doing very good! Let us try another spell.\n")
time.sleep(3)

spell2 = ""

while spell2 not in ["aquafera"]:
    spell2 = input("Type 'Aquafera' in order to produce a stream of water.\n").strip().lower()
    if spell2 not in ["aquafera"]:
        time.sleep(1)
        print("Invalid answer. Please type 'Aquafera' to try out the spell.\n")
        time.sleep(2)
        continue

        # loop created with help of ChatGBT

if spell2 == "aquafera":
    time.sleep(1)
    print("I now placed an empty bucket in front of you. Try to fill it with water, but be careful. \nI am not the one, who is going to clean up your mess.\n")
    time.sleep(5)

    while True:
        mana2 = input("Type in a number between 1 and 10 to choose the appropriate amount of mana.\n").strip()
        if not mana2.isdigit():
            print("This is not a number, my apprentice.Try again.\n")
            time.sleep(2)
            continue

            # loop created with help of ChatGBT

        mana2 = int(mana2)
        if mana2 > 10 or mana2 < 1:
            print("Please enter a number between 1 and 10.\n")
            time.sleep(2)
            continue

        elif mana2 > 5 and mana2 <= 8:
            print("Good job! You filled your bucket within seconds and you didn't flood the whole classroom.\n")
            time.sleep(3)
            break

        elif mana2 <= 4 and mana2 >= 1:
            print("Try it with a little more force, or you will have to wait here until tomorrow to fill your bucket.\n")
            time.sleep(3)
            continue

        else:
            print("Careful! I didn't want to go swimming today. Try it a little softer.\n")
            time.sleep(3)
            continue

print ("You now learned your first 2 spells. Let's put you to a little test now and see what you can do already.\n")
time.sleep(5)
print ("We brought you into a completely empty room. In front of you there are two doors.\n")
time.sleep(5)
print ("Behind each you will be confronted with a hindrance, that you will have to surpass in order to get out.\n")
time.sleep(5)

door = ""

while door not in ["left", "right"]:
    door = input("Type 'left' or 'right' to choose one of the doors.\n").strip().lower()
    if door not in ["left", "right"]:
        time.sleep(1)
        print ("Invalid answer. Please choose either 'left' or 'right'.\n")
        time.sleep(2)

if door == "left":
    time.sleep(1)
    print ("You enter and behind you the door falls shut with a loud *whum*.\n")
    time.sleep(4)
    print ("You feel an intense warmth and when you look up, there is a fire in front of you. It has already filled the whole room with smoke \nand you have to cough.\n")
    time.sleep(8)

    spell3 = ""
    while True:
        spell3 = input ("Which of the spells, you just learned, are you going to choose to get you out of this?\n").strip().lower()

        if spell3 not in ["aquafera", "galea"]:
            time.sleep(1)
            print ("That is not a valid spell. Quick, it is getting warmer.\n")
            time.sleep(3)
            continue

        if spell3 == "galea":
            time.sleep(1)
            print ("That was not a good idea. As you use the wind spell, the fire feeds on the additional air and the flames rise even higher. \nQuick, think of something else.\n")
            time.sleep(7)
            continue

        if spell3 == "aquafera":
            time.sleep(1)
            print ("Perfect choice in just the right moment.\n")

            time.sleep(3)

            while True:
                mana3 = input("Type in a number between 1 and 10 to choose the appropriate amount of mana.\n").strip()
                if not mana3.isdigit():
                    print("This is not a number, my apprentice.Try again.\n")
                    time.sleep(3)
                    continue

                    # loop created with help of ChatGBT

                mana3 = int(mana3)
                if mana3 > 10 or mana3 < 1:
                    print("Please enter a number between 1 and 10.\n")
                    time.sleep(3)
                    continue

                elif mana3 > 8 and mana3 <= 10:
                    print(
                        "Phew! A massive stream of water emerges and manages to put out all the flames.\n")
                    time.sleep(4)
                    break

                else:
                    print(
                        "That is not enough. The fire is very strong. Use all the strength you have, or you will get burned!\n")
                    time.sleep(5)
                    continue
            break

    print ("With all the flames out of the way, you can see a door at the other end of the room. You open it and can finally breathe some fresh air again.\n")
    time.sleep(5)
    print ("Good job, apprentice! You mastered your first challenge. I see a lot of talent in you and am excited to see you become a great wizard \nat our Academy.")

else:
    time.sleep(1)
    print("You enter and behind you the door falls shut with a loud *whum*.\n")
    time.sleep(2)
    print("As you look to your feet, you see, that the room is rapidly filling itself with water. You look up and try to see to the other end of the room.\n")
    time.sleep(5)
    print ("The wall on the other side is far away, but you notice a small detail: A stone with a glowing rune on it, that stands out of the wall. \nIf you could just press it, it will surely be your way out of this misery.\n ")
    time.sleep(5)
    print ("But the water is already at your chest. You don't have enough time to swim to the other side and if you don't hurry up, you will have to drown!\n")
    time.sleep(2)

    spell4 = ""
    while True:
        spell4 = input(
            "Which of the spells, you just learned, are you going to choose to get you out of this?\n").strip().lower()

        if spell4 not in ["aquafera", "galea"]:
            time.sleep(1)
            print("That is not a valid spell. Quick, the water is rising higher!\n")
            time.sleep(3)
            continue

        if spell4 == "aquafera":
            time.sleep(1)
            print("That was not a good idea. As you use the water spell, the water is rising even quicker and you have to start swimming to keep \nyour head over the surface. Quick, think of something else.\n")
            time.sleep(7)
            continue

        if spell4 == "galea":
            time.sleep(1)
            print("Perfect choice in just the right moment.\n")

            time.sleep(3)

            while True:
                mana4 = input("Type in a number between 1 and 10 to choose the appropriate amount of mana.\n").strip()
                if not mana4.isdigit():
                    print("This is not a number, my apprentice.Try again.\n")
                    time.sleep(3)
                    continue

                    # loop created with help of ChatGBT

                mana4 = int(mana4)
                if mana4 > 10 or mana4 < 1:
                    print("Please enter a number between 1 and 10.\n")
                    time.sleep(3)
                    continue

                elif mana4 > 8 and mana4 <= 10:
                    print("Phew! A strong blast of wind emerges, with enough force the push the glowing rune stone at the other end.\n")
                    time.sleep(5)
                    break

                else:
                    print("That is not enough. The wind is not strong enough to reach the other side and the room is almost completely filled with water now! \nUse all your strength now!\n")
                    time.sleep(7)
                    continue

            break

    print(
        "A door opens on the far wall and all the water is starting to flow outside, taking you with it. Soon you find yourself sitting outside, \nsoggy but alive.\n")
    time.sleep(5)
    print(
        "Good job, apprentice! You mastered your first challenge. I see a lot of talent in you and am excited to see you become a great wizard \nat our Academy.")


#I used ChatGBT to:
#learn how to check if an input is a number
#also took the .strip().lower() idea from ChatGBT

