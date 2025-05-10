import time

MAX_INVENTORY_SIZE = 5
REQUIRED_INGREDIENTS = ["carrot", "mushroom", "healing herbs", "onion", "bottle of water"]
inventory = []
current_room = "forest clearing"

rooms = {
    "forest clearing": [
        {"name": "bottle of water", "type": "ingredient", "description": "Fresh water from the mountains."},
        {"name": "stone", "type": "junk", "description": "Just an ordinary stone."},
        {"name": "mushroom", "type": "ingredient", "description": "A mushroom! And it's an edible one, lucky you."},
        {"name": "key", "type": "tool", "description": "A rusty old key."}
    ],
    "old garden": [
        {"name": "carrot", "type": "ingredient", "description": "Mmh, a crunchy carrot."},
        {"name": "onion", "type": "ingredient", "description": "An onion a day keeps the doctor away... or so I've heard."},
        {"name": "healing herbs", "type": "ingredient", "description": "These will restore your strength in no time, you will see."},
        {"name": "shovel", "type": "junk", "description": "A forgotten gardening utensil."}
    ]
}

locked_rooms = {
    "old garden": True
}

def get_current_room_items():
    return rooms[current_room]

def wait(seconds):
    time.sleep(seconds)

def show_inventory():
    if not inventory:
        print("Your bag is empty.")
    else:
        print("What's in your bag:")
        for item in inventory:
            print(f"- {item['name']}")

def show_room_items():
    items = get_current_room_items()
    if not items:
        print("There's nothing in here.")
    else:
        print("Let's see what we have in here:")
        for item in items:
            print(f"- {item['name']}")

def pick_up(item_name):
    items = get_current_room_items()
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your bag is full. Drop something to make space.")
        return

    for item in items:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items.remove(item)
            print(f"You have picked up {item['name']}.")
            return

    print(f"{item_name} is not here.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            get_current_room_items().append(item)
            print(f"You dropped {item['name']}.")
            return
    print(f"{item_name} is not in your bag.")

def examine(item_name):
    for item in inventory + get_current_room_items():
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: {item['description']}")
            return
    print(f"{item_name} is neither here nor in your bag.")

def use(item_name):
    if item_name.lower() == "soup":
        needed = REQUIRED_INGREDIENTS.copy()
        for item in inventory:
            if item["name"] in needed:
                needed.remove(item["name"])
        if not needed:
            print("You've got all the ingedrients and can now make a warm and delicious healing soup ... 🍲")
            wait (3)
            print("Smells wonderful! You eat and feel a new energy in your body.")
            wait(1)
            print("You win 🌱")
            exit()
        else:
            print("You still need for your soup:")
            for missing in needed:
                print(f"- {missing}")
        return

    if item_name.lower() == "key":
        if any(item["name"].lower() == "key" for item in inventory):
            if locked_rooms["old garden"]:
                locked_rooms["old garden"] = False
                print("You use the key and the gate opens.")
                global current_room
                current_room = "old garden"
                print("You go inside.")
            else:
                print("The gate is already open.")
        else:
            print("You don't have a key.")
        return

    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "ingredient":
                print(f"You prepare the {item['name']}  – it will be used for the soup.")
            elif item["type"] == "junk":
                print(f"Nothing much to do with a {item['name']}.")
            else:
                print(f"You use {item['name']}, but nothing happens.")
            return
    print(f"{item_name} is not in your bag.")

def show_help():
    print("\navailable commands:")
    print("  inventory             - shows what is in your bag")
    print("  look                  - shows what items are in the area")
    print("  pickup [item]         - picks up an item (e.g. pickup carrot)")
    print("  drop [item]           - removes an item from your bag")
    print("  examine [item]        - gives you additional information for an item (in your bag and in the area)")
    print("  use [item]            - tries out, if the item is of any use for you")
    print("  use soup              - cooks your soup")
    print("  go to [place]         - brings you to another place (forest clearing (that's where you start) or old garden)")
    print("  help                  - shows this list of commands")
    print("  quit                  - ends the game")

def game_loop():
    print("🌲🍄🥕🍲FOREST SOUP🍲🥕🍄🌲")
    wait(1)
    print("Greetings, warrior! I see you have come a far way and what lies ahead is dark and full of dangers .\n")
    wait(5)
    print("I suggest you make yourself a nourishing soup before you head into your next adventure.\n")
    wait(3)
    print("🌲🌳🌲In this forest you will find everything you need.🌳🌲🌳\n")
    wait(3)
    print("type 'help' for a list of all available commands.")

    while True:
        command = input("\n> ").strip().lower()

        if command == "help":
            show_help()
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("go to"):
            target = command[6:]
            if target not in rooms:
                print("This place does not exist.")
            elif target == "old garden" and locked_rooms["old garden"]:
                print("Wow, looks like an abandoned garden! But the gate is closed...")
            else:
                global current_room
                current_room = target
                print(f"You go to the {target}.")
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("thanks for playing! 🍂")
            break
        else:
            print("Unknown request. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    game_loop()