# CONSTANTS
VALID_SPELLS = ["galea", "aquafera"]
MIN_MANA, MAX_MANA = 1, 10

# IMPORTS
import time

# FUNCTIONS

def wait(seconds):
    time.sleep(seconds)

def get_spell_input(expected_spell):
    while True:
        spell = input(f"Type '{expected_spell.capitalize()}' to try out the spell.\n").strip().lower()
        if spell == expected_spell:
            return spell
        print(f"Invalid answer. Please type '{expected_spell.capitalize()}'.")
        wait(2)

def get_mana_input():
    while True:
        mana = input(f"Type in a number between {MIN_MANA} and {MAX_MANA} to choose the appropriate amount of mana.\n").strip()
        if not mana.isdigit():
            print("This is not a number, my apprentice. Try again.\n")
            wait(2)
            continue
        mana = int(mana)
        if MIN_MANA <= mana <= MAX_MANA:
            return mana
        print(f"Please enter a number between {MIN_MANA} and {MAX_MANA}.\n")
        wait(2)

def mana_challenge(success_range, too_weak_range, too_strong_range=None, too_strong_message=None, weak_message="", success_message=""):
    while True:
        mana = get_mana_input()
        if mana in success_range:
            print(success_message)
            wait(3)
            return True
        elif mana in too_weak_range:
            print(weak_message)
        elif too_strong_range and mana in too_strong_range and too_strong_message:
            print(too_strong_message)
        else:
            print("That's not quite right. try again.")
        wait(3)

# lessons
def lesson_wind():
    print("Let's begin with your first spell casting lesson.\n")
    wait(3)
    print("'Galea' is our first spell. It produces a force of wind.")
    wait(3)
    get_spell_input("galea")
    print("Do you see the piece of cloth I placed in front of you? Your goal is to get it off the table with your wind spell. \nBut careful: we don't want it flying through the whole room!\n")
    wait(5)
    mana_challenge(
        success_range=range(4,7),
        too_weak_range=range(1,4),
        too_strong_range=range(7,11),
        too_strong_message="Careful there! That was way too strong. The cloth is flying through the whole room. Try it a little softer.\n",
        weak_message="That was not strong enough. Try it with a little more force.\n",
        success_message="Perfect! Your piece of cloth slides elegantly off the table and lands on the ground a few meters away from you.\n"
    )

def lesson_water():
    print("Our next spell is called 'Aquafera'. It produces a stream of water.\n")
    wait(3)
    get_spell_input("aquafera")
    print("I know placed an empty bucket in front of you. Try to fill it with water, but be careful. \nI am not the one, who is going to clean up your mess.\n")
    wait(5)
    mana_challenge(
        success_range=range(5,8),
        too_weak_range=range(1,5),
        too_strong_range=range(8,11),
        too_strong_message="Careful! I didn't want to go swimming today. Try it a little softer.\n",
        weak_message="Try it with a little more force, or you will have to wait here until tomorrow to fill your bucket.\n",
        success_message="Good job! You filled your bucket within seconds and you didn't flood the whole classroom.\n"
    )
# choose between 2 rooms
def choose_door():
    while True:
        door = input("Type 'left' or 'right' to choose a door.\n").strip().lower()
        if door in ["left", "right"]:
            return door
        print("Invalid answer. Please type 'left' or 'right'.")
        wait(2)

#rooms and what happens inside
def fire_room():
    print("You feel an intense warmth and when you look up, there is a fire in front of you. It has already filled the whole room with smoke \nand you have to cough.\n")
    wait(8)
    while True:
        spell = input("Which of the spells, you just learned, are you going to choose to get you out of this?\n").strip().lower()
        if spell == "aquafera":
            print("Perfect choice in just the right moment.\n")
            wait(2)
            mana_challenge(
                success_range=range(8,11),
                too_weak_range=range(1,8),
                weak_message="That is not enough. The fire is very strong. Use all the strength you have, or you will get burned!\n",
                success_message="Phew! A massive stream of water emerges and manages to put out all the flames.\n"
            )
            break
        elif spell == "galea":
            print("That was not a good idea. As you use the wind spell, the fire feeds on the additional air and the flames rise even higher. \nQuick, think of something else.\n")
            wait(3)
        else:
            print("That's not a valid spell!")
            wait(2)

    print("With all the flames out of the way, you can see a door at the other end of the room. You open it and can finally breathe some fresh air again.\n")
    wait(5)

def flood_room():
    print("As you look to your feet, you see, that the room is rapidly filling itself with water. You look up and try to see to the other end of the room.\n")
    wait(5)
    print("The wall on the other side is far away, but you notice a small detail: A stone with a glowing rune on it, that stands out of the wall. \nIf you could just press it, it will surely be your way out of this misery.\n")
    wait(5)
    print("But the water is already at your chest. You don't have enough time to swim to the other side and if you don't hurry up, you will have to drown!\n")
    wait(2)

    while True:
        spell = input("Which of the spells, you just learned, are you going to choose to get you out of this?\n").strip().lower()
        if spell == "galea":
            print("Perfect choice in just the right moment.\n")
            wait(2)
            mana_challenge(
                success_range=range(8,11),
                too_weak_range=range(1,8),
                weak_message="That is not enough. The wind is not strong enough to reach the other side and the room is almost completely filled with water now! \nUse all your strength now!\n",
                success_message="Phew! A strong blast of wind emerges, with enough force the push the glowing rune stone at the other end.\n"
            )
            break
        elif spell == "aquafera":
            print("That was not a good idea. As you use the water spell, the water is rising even quicker and you have to start swimming to keep \nyour head over the surface. Quick, think of something else.\n")
            wait(7)
        else:
            print("That's not a valid spell!")
            wait(2)

    print("A door opens on the far wall and all the water is starting to flow outside, taking you with it. Soon you find yourself sitting outside, \nsoggy but alive.\n")
    wait(5)


#MAIN PROGRAM

def main():
    print("We wish you a very warm welcome at Astarion - the most renowned Academy for Witchcraft in the country!\n")
    wait(5)
    print("Here you will have the chance to discover unknown talents and prove yourself worthy to be a part of witchcraft society.\nDo you have the courage and the wit to master this challenge? Let's find out!\n")
    wait(8)
    print("I am Professor Nutmeg. I will teach you the basics of wizardy and will help you master your first challenges.\n")
    wait(5)

    # spell casting lessons
    lesson_wind()
    print("You are doing very good! Let us try another spell.\n")
    wait(3)

    lesson_water()
    print("Excellent control!\n")
    wait(2)

    # first test
    print("You now learned your first 2 spells. Let's put you to a little test now and see what you can do already.\n")
    wait(5)
    print("We brought you into a completely empty room. In front of you there are two doors.\n")
    wait(5)
    print("Behind each you will be confronted with a hindrance, that you will have to surpass in order to get out.\n")
    wait(5)
    door = choose_door()
    print("You enter and behind you the door falls shut with a loud *whum*.\n")
    wait(4)
    if door == "left":
        fire_room()
    else:
        flood_room()

    # end
    print("Good job, apprentice! You mastered your first challenge. I see a lot of talent in you and am excited to see you become a great wizard \nat our Academy.")

# START
if __name__ == "__main__":
    main()


### I used ChatGBT to:
# figure out how to best restructure my game with the functions
# explain to me how the main function is used
# give me an idea how to solve mistakes