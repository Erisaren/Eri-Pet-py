import random

import sys
import time
# import pickle

# TODO Put an ailment system from playing too much and from outdoor system.
# TODO Put an outdoor system to play and out.
# TODO Tweak happiness system depending on basic stats and play time.
# TODO Fix hygiene.
# TODO pickle 101 to be able to save and load Pet' state.
# TODO Random activities.
'''
Recommendations for Implementing Random Activities and Movement:

Define Activity Pool: Create a list of activities the pet can engage in (e.g., sleep, play with toys, explore, eat, drink).
Assign Weighted Probabilities: Adjust the likelihood of each activity based on factors like time of day, energy levels, happiness, and recent events.
Implement a Random Selection Function: Write a function that chooses an activity from the pool based on the weighted probabilities.
Integrate with Main Loop: Incorporate the random activity selection into the main game loop, executing the chosen activity at regular intervals.
Create a Navigation System: Designate areas for different activities (e.g., bed for sleeping, play area for playing).
Implement Movement Logic: Allow the pet to move between these areas based on the selected activity.
'''
class Pet(object):
    def __init__(self, owner, name, gender, age):  # Defining one-time values for the pet.
        self._owner = owner
        self._name = name
        self._gender = gender
        self._age = age

        self._likefood = ["apple", "grapes", "mango", "pineapple", "watermelon"]
        self._dislikefood = ["apple", "grapes", "mango", "pineapple", "watermelon"]
        self._lf = (random.choice(self._likefood))
        self._df = (random.choice(self._dislikefood))
        self._likedrink = ["juice", "milk", "soda", "water", "yoghurt"]
        self._dislikedrink = ["juice", "milk", "soda", "water", "yoghurt"]
        self._ld = (random.choice(self._likedrink))
        self._dd = (random.choice(self._dislikedrink))

        self._sickfoodhigh = 0  # Setting sickness gauge
        self._sickfoodlow = 0  # to fire an ailment
        self._sickdrinkhigh = 0  # and decrease
        self._sickdrinklow = 0  # the health system.
        self._poop = 0
        self._pee = 0

        self._satiety = random.randint(15, 75)  # 100 means satiated.
        self._hydration = random.randint(15, 75)  # 100 means hydrated.
        self._energy = random.randint(15, 75)  # 100 means energised.
        self._health = 100  # 100 means healthy.
        self._cleanliness = random.randint(35, 75)  # 100 means clean.
        self._happiness = round((self._satiety + self._hydration + self._cleanliness) / 3)

    def feed_refresh(self):  # Stat refresher for hunger system.
        if self._satiety >= 100:
            print(f"{self._name} is satiated.")
            self._satiety = 100
        elif self._satiety <= 0:
            print(f"{self._name} is starving!")
            self._satiety = 0
        elif 0 < self._satiety < 100:
            print(f"{self._name}'s satiety level: {self._satiety}.")
        return

    def drink_refresh(self):  # Stat refresher for thirst system.
        if self._hydration >= 100:
            print(f"{self._name} is hydrated.")
            self._hydration = 100
        elif self._hydration <= 0:
            print(f"{self._name} is thirsty!")
            self._hydration = 0
        elif 0 < self._hydration < 100:
            print(f"{self._name}'s hydration level: {self._hydration}.")
        return

    def bath_refresh(self):  # Stat refresher for hygiene system.
        if self._poop <= 0 and self._pee <= 0:
            print(f"{self._name} is squeaky clean.")
        elif self._poop <= 25 and self._pee <= 25:
            print(f"{self._name} is clean.")

        if 25 < self._poop < 51:
            print(f"{self._name} needs to go poop.")
        elif 25 < self._pee < 51:
            print(f"{self._name} needs to go pee.")
        elif (25 < self._poop < 50) and (25 < self._pee < 50):
            print(f"{self._name} needs to visit the bathroom.")

        if self._poop > 50:
            self._cleanliness = 0
            print(f"{self._name} has pooped on the floor.")
            self._poop = 0
        elif self._pee > 50:
            self._cleanliness = 0
            print(f"{self._name} has peed on the floor.")
            self._pee = 0
        elif (self._poop > 50) and (self._pee > 50):
            self._cleanliness = 0
            print(f"{self._name} has left a mess on the floor.")
            self._poop = 0
            self._pee = 0
        return

    def heal_refresh(self):  # Stat refresher for health system.
        while True:
            if self._satiety > 100:
                self._sickfoodhigh = (self._satiety - 100)
                break

            elif self._satiety < 0:
                self._sickfoodlow = (0 - self._satiety)
                break

            if self._hydration > 100:
                self._sickdrinkhigh = (self._hydration - 100)
                break

            elif self._hydration < 0:
                self._sickdrinklow = (0 - self._hydration)
                break

            sick = self._sickfoodhigh + self._sickfoodlow + self._sickdrinkhigh + self._sickdrinklow

            if 0 < sick < 11:
                self._health -= 5
                break

            elif 11 < sick < 31:
                self._health -= 10
                break

            elif 31 < sick < 61:
                self._health -= 15
                break

            elif 61 < sick < 101:
                self._health -= 20
                break

            elif sick > 100:
                self._health += 25
                break

            if 0 < self._health < 25:
                print(f"{self._name} looks very sick.")
                break
            elif 25 < self._health < 50:
                print(f"{self._name} looks sick.")
                break
            elif 50 < self._health < 75:
                print(f"{self._name} looks feverish.")
                break
            elif 75 < self._health < 100:
                print(f"{self._name} looks a bit feverish.")
                break
            elif self._health == 100:
                print(f"{self._name} is healthy.")
                break
            elif self._health <= 0:
                print(f"{self._name}: Good-Bye, {self._owner}...")
                break

    def feed(self):  # Give food to the pet.
        while self._satiety < 100:
            print("Please feed your pet something. You can choose between 'apple' 'grapes' 'mango' 'pineapple' or "
                  "'watermelon': ")
            feed = input()

            if feed == self._lf:
                print(f"{self._name}: Yum!")
                print(f"It seems {self._name} likes " + self._lf + " a lot!")
                self._satiety += 15
                self._happiness += 5
                self._poop += 5
                break

            elif feed == self._df:
                print(f"{self._name}: Yuck!")
                print(f"It seems {self._name} dislikes " + self._df + " a lot!")
                self._satiety += 5
                self._happiness -= 10
                self._poop += 2
                break

            elif feed != self._lf and feed != self._df:
                print(f"{self._name}: Nom!")
                print(f"{self._name} seems fine with " + feed + ".")
                self._satiety += 10
                self._happiness += 1
                self._poop += 3
                break

            else:
                break

        return

    def drink(self):  # Give drink to the pet.

        while self._hydration < 100:
            print("Please give any beverage to your pet. You can choose between 'juice' 'milk' 'soda' 'water' or "
                  "'yoghurt': ")
            drink = input()

            if drink == self._ld:
                print(f"{self._name}: Yum!")
                print(f"It seems {self._name} likes " + self._ld + " a lot!")
                self._hydration += 15
                self._happiness += 5
                self._pee += 5
                break

            elif drink == self._dd:
                print(f"{self._name}: Yuck!")
                print(f"It seems {self._name} dislikes " + self._dd + " a lot!")
                self._hydration += 5
                self._happiness -= 10
                self._pee += 2
                break

            elif drink != self._ld and drink != self._dd:
                print(f"{self._name}: Nom!")
                print(f"{self._name} seems fine with " + drink + ".")
                self._hydration += 10
                self._happiness += 1
                self._pee += 3
                break

        return

    def bath(self):  # Give bath to the pet.
        print(f"You bathe {self._name}.")

        while self._cleanliness < 100:
            self._cleanliness = 100
            self._poop = 0
            self._pee = 0

        return

    def sleep(self):  # Tuck the pet in bed.
        while True:
            if self._energy < 100:
                print(f"{self._name} is sleeping.")
                self._energy += 25
                time.sleep(1)
                if self._energy > 100:
                    self._energy = 100

            elif self._energy >= 100:
                print(f"{self._name} is feeling energetic already!")
                self._energy = 100
                break
        return

    def heal(self):  # Heal the pet.

        if 0 < self._health < 100:
            print(f"You give {self._name} a medicine.")
            self._health += 25

        if self._health == 100:
            print(f"{self._name} is not sick.")

        elif self._health <= 0:
            print(f"Your pet is in a better world now.")

        return

    def stats(self):  # Defining stats.

        print(f"Satiety: {self._satiety}")
        print(f"Hydration: {self._hydration}")
        print(f"Hygiene: {self._cleanliness}")
        print(f"Energy: {self._energy}")
        print(f"Happiness: {self._happiness}")
        print(f"Health: {self._health}")


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
        bot.feed_refresh()
        bot.drink_refresh()
        bot.bath_refresh()
        bot.heal_refresh()
        print(bot.stats())
        print("""
        #----------------MENU--------------#
        # \"F\" for [feed], \"D\" for [drink]  #
        # \"B\" for [bath]                     #
        # \"Z\" for [sleep],  \"X\" for [heal] #
        # \"Q\" to quit:                      #
        #----------------------------------#
        """)
        prompt = input()

        if prompt == "F" or prompt == "f":
            bot.feed()

        elif prompt == "D" or prompt == "d":
            bot.drink()

        elif prompt == "B" or prompt == "b":
            bot.bath()

        elif prompt == "Z" or prompt == "z":
            bot.sleep()

        elif prompt == "X" or prompt == "x":
            bot.heal()

        elif prompt == "Q" or prompt == "q":
            sys.exit(0)


if __name__ == "__main__":
    main()
