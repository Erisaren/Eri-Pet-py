import random
import time
import sys


class Pet(object):
    def __init__(self, owner, name, gender, age):  # defining values.
        self._owner = owner
        self._name = name
        self._gender = gender
        self._age = age

        #  Random stats at start.
        self._hunger = random.randint(15, 75)
        self._thirst = random.randint(15, 75)
        self._smell = random.randint(15, 75)
        self._energy = random.randint(15, 75)
        self._poop_on_floor = 0

        #  Happiness and Health calculation.
        self._happiness = (self._hunger + self._thirst + self._smell) / 3
        self._health = (self._energy + self._hunger + self._thirst) / 3

        # Rounding so that 0.5 = 0.
        self._happiness = round(self._happiness)
        self._health = round(self._health)

    def stats(self):  # Displays the stats.

        print(f"Satiety: {self._hunger}")
        print(f"Quench: {self._thirst}")
        print(f"Hygiene: {self._smell}")
        print(f"Energy: {self._energy}")
        print(f"Happiness: {self._happiness}")
        print(f"Health: {self._health}")
        if self._poop_on_floor > 5:
            print(f"Poop: {self._name} has pooped!")
        else:
            print("Poop: No poop.")

    def feed(self):  # Give food to the pet.

        self._hunger += 15
        self._poop_on_floor += 5
        print(f"{self._name}: Yum!")
        if self._hunger > 100 and self._poop_on_floor > 100:
            self._hunger = 100
            self._poop_on_floor = 100
        elif self._poop_on_floor > 100:
            self._poop_on_floor = 100
        elif self._hunger > 100:
            self._hunger = 100
        return

    def drink(self):  # Give water to the pet.

        self._thirst += 15
        self._poop_on_floor += 2
        print(f"{self._name}: Hmm!")
        if self._thirst > 100 and self._poop_on_floor > 100:
            self._thirst = 100
            self._poop_on_floor = 100
        elif self._poop_on_floor > 100:
            self._poop_on_floor = 100
        elif self._thirst > 100:
            self._thirst = 100
        return

    def clean(self):  # Dust the pet.
        print(f"You clean up {self._name}.")
        self._smell += 45
        self._poop_on_floor -= 15
        if self._smell > 100 and self._poop_on_floor > 100:
            self._smell = 100
            self._poop_on_floor = 100
        elif self._poop_on_floor > 100:
            self._poop_on_floor = 100
        elif self._smell > 100:
            self._smell = 100
        return

    def bath(self):  # Give bath to the pet.
        print(f"You bathe {self._name}.")
        self._smell = 100
        self._poop_on_floor = 0
        if self._smell > 100 and self._poop_on_floor > 100:
            self._hunger = 100
            self._poop_on_floor = 100
        elif self._poop_on_floor > 100:
            self._poop_on_floor = 100
        elif self._smell > 100:
            self._smell = 100
        return

    def sleep(self):  # Tuck the pet in bed.
        while True:
            if 0 < self._energy < 100:
                print(f"{self._name} is sleeping.")
                self._energy += 25
                time.sleep(1)
                if self._energy > 100:
                    self._energy = 100

            elif self._energy == 100:
                print(f"{self._name} is feeling energetic!")
                break

    def heal(self):  # Heal the pet.
        if self._health < 100:
            print(f"You heal up {self._name}.")
            self._health += 30
            if self._health > 100:
                self._health = 100
            return
        elif self._health == 100:
            print(f"{self._name} is not sick.")
            return

    def status(self):  # Check the mood.
        print("Satiety:")
        if self._hunger == 100:
            print(f"{self._name} is not hungry.")
        elif 80 <= self._hunger < 100:
            print(f"{self._name} is a little peckish.")
        elif 50 <= self._hunger < 80:
            print(f"{self._name} is hungry.")
        elif 25 <= self._hunger < 50:
            print(f"{self._name} is very hungry.")
        else:
            print(f"{self._name} is starving.")

        print("Quench:")
        if self._thirst == 100:
            print(f"{self._name} is not thirsty.")
        elif 80 <= self._thirst < 100:
            print(f"{self._name} is a little parched.")
        elif 50 <= self._thirst < 80:
            print(f"{self._name} is thirsty.")
        elif 25 <= self._thirst < 50:
            print(f"{self._name} is very thirsty.")
        else:
            print(f"{self._name} is drained.")

        print("Hygiene:")
        if self._smell == 100:
            print(f"{self._name} is squeaky clean.")
        elif 80 <= self._smell < 100:
            print(f"{self._name} is a little dirty.")
        elif 50 <= self._smell < 80:
            print(f"{self._name} is dirty.")
        elif 25 <= self._smell < 50:
            print(f"{self._name} is very dirty.")
        else:
            print(f"{self._name} is stinking.")

        print("Energy:")
        if self._energy == 100:
            print(f"{self._name} is energetic.")
        elif 80 <= self._energy < 100:
            print(f"{self._name} is awake.")
        elif 50 <= self._energy < 80:
            print(f"{self._name} is somewhat drowsy.")
        elif 25 <= self._energy < 50:
            print(f"{self._name} is very drowsy.")
        else:
            print(f"{self._name} is sleepy.")

        print("Happiness:")
        if 80 <= self._happiness <= 100:
            print(f"{self._name} seems ecstatic.")
        elif 50 <= self._happiness < 80:
            print(f"{self._name} seems in high spirits.")
        elif 25 <= self._happiness < 50:
            print(f"{self._name} seems kind of down.")
        else:
            print(f"{self._name} seems mad and depressed.")

        print("Health:")
        if 80 <= self._health <= 100:
            print(f"{self._name} seems healthy.")
        elif 50 <= self._health < 80:
            print(f"{self._name} is under the weather.")
        elif 25 <= self._health < 50:
            print(f"{self._name} is kind of sick.")
        elif 5 <= self._health < 25:
            print(f"{self._name} is sick.")
        elif 1 <= self._health < 5:
            print(f"{self._name} is dying.")
        else:
            if self._health <= 0:
                self._health = 0
            print(f"{self._name} is no more...")
            sys.exit(0)


def main():
    print("Welcome to Erisaren's sample pet game!")
    time.sleep(1)
    print("Let's head to the pet creation process.\n")
    time.sleep(1)
    owner = str(input("Please enter your name: "))
    answer = str(input(f"Are you okay with {owner.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer in {"Y", "y"}:
            owner = owner.capitalize()  # Capitalise the name.
            break

        else:
            owner = input("Please enter your name: ")
            answer = str(input(f"Are you okay with {owner.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    time.sleep(1)

    print(f"Dear {owner}, we will create your pet!")
    name = str(input("Please enter your pet's name: "))
    answer1 = str(input(f"Are you okay with {name.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer1 in {"Y", "y"}:
            name = name.capitalize()
            break

        else:
            name = input("Please enter your pet's name: ")
            answer1 = str(input(f"Are you okay with {name.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    time.sleep(1)

    gender = str(input("What is your pet's gender?\nPress \"M\" for male or \"F\" for female: "))
    answer2 = str(input(f"Are you okay with {gender.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer2 in {"Y", "y"}:
            if gender in {"M", "m"}:
                gender = "male"
                break

            elif gender in {"F", "f"}:
                gender = "female"
                break
        else:
            gender = input("Please enter your pet's gender: ")
            answer2 = str(input(f"Are you okay with {gender.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    time.sleep(1)

    print("Processing.")
    time.sleep(1)
    print("Processing..")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)

    #  Some initialisations.
    age = 0
    prompt = " "
    bot = Pet(owner, name, gender, age)  # Instantiation.
    time.sleep(2)

    print(f"Pet sheet: [{name}]: It is a {gender} and its caregiver is {owner}.")

    print(
        f"\n{name}: Greetings, {owner}! I am happy to see you!\nI am excited to live so many adventures with you!\n"
        f"I can eat, drink, shower, sleep, or play with you "
        f" if you enter each of the following commands:\n")

    while prompt != "Q" or prompt != "q":
        print(bot.stats())
        print("""
        #----------------MENU--------------#
        # \"F\" for [feed], \"D\" for [drink]  #
        # \"C\" for [clean], \"B\" for [bath]  #
        # \"Z\" for [sleep],  \"X\" for [heal] #
        # \"H\" for [status],  \"Q\" to quit:  #
        #----------------------------------#
        """)
        prompt = input()

        if prompt == "F" or prompt == "f":
            bot.feed()

        elif prompt == "D" or prompt == "d":
            bot.drink()

        elif prompt == "C" or prompt == "c":
            bot.clean()

        elif prompt == "B" or prompt == "b":
            bot.bath()

        elif prompt == "Z" or prompt == "z":
            bot.sleep()

        elif prompt == "X" or prompt == "x":
            bot.heal()

        elif prompt == "H" or prompt == "h":
            print(bot.status())

        elif prompt == "Q" or prompt == "q":
            sys.exit(0)


if __name__ == "__main__":
    main()
