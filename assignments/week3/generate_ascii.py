import random
import time

print("*** Star Simulator ***\n")
time.sleep(2)
print("Welcome! Here you can create your own sky of stars with a personal message.\n")
time.sleep(4)

while True:
    width_input = input("How wide should your sky be? (Type e.g. 40)")
    if width_input.isdigit():
        width = int(width_input)
        break
    else:
        print("Please enter a valid number.")
        continue

while True:
    height_input = input("How tall should your sky be? (Type e.g. 10): ")
    if height_input.isdigit():
        height = int(height_input)
        break
    else:
        print("Please enter a valid number.")
        continue

name = input("What word or short message should appear in the sky?")

print("\nprocessing your input...\n")
time.sleep(3)

sky = [" ", ".", "*"]

line_index = height // 2

for y in range(height):
    line = [random.choice(sky) for _ in range(width)]

    if y == line_index:
        name_position = random.randint(0, width - len(name))

        for i, char in enumerate(name):
            line[name_position + i] = char

        for x in range(width):
            if line[x] == " ":
                line[x] = random.choice(sky)

    print("".join(line))

### I used ChatGBT to:
# understand how to use the for loops in order to create the picture how I wanted it to look like