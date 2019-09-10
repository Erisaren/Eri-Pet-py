import random
import time
import textwrap


class Droid:
    def __init__(self, owner, name, gender, model, age):

        self._owner = owner.capitalize()
        self._name = name.capitalize()
        self._gender = gender
        self._model = model
        self._age = age  # Should increment for day % 86400 = 0

        self._hunger = random.randint(15, 75)  # Use the feed function.
        self._thirst = random.randint(15, 75)  # Use the drink function.
        self._smell = random.randint(15, 75)  # Use the bathe function.
        self._loneliness = random.randint(15, 75)  # Use the play function.
        self._energy = random.randint(15, 75)  # Use the sleep function.

        self._happiness = (round(self._hunger + self._thirst + self._smell) / 3)
        self._health = (round(self._hunger + self._thirst + self._energy) / 3)

        self._game_over = False  # Not implemented.
        self._poop_on_floor = 0  # Use the clean function.

    def stats(self):
        print(textwrap.dedent("""._._._._._._._._._._._._"""))
        print(f"Hunger: {self._hunger}")
        print(f"Thirst: {self._thirst}")
        print(f"Hygiene: {self._smell}")
        print(f"Loneliness: {self._loneliness}")
        print(f"Energy: {self._energy}")
        print(f"Happiness: {self._happiness}")
        print(f"Health: {self._health}")
        print(textwrap.dedent("""._._._._._._._._._._._._"""))

    def feed(self, food):  # Based on favourite food of each robot.
        if food == "lightning bolt" and self._model == "electric":
            self._hunger -= 15
            self._poop_on_floor += 0.5
            return True
        elif food == "coal" and self._model == "coal":
            self._hunger -= 15
            self._poop_on_floor += 0.5
            return True
        elif food == "ice" and self._model == "steam":
            self._hunger -= 15
            self._poop_on_floor += 0.5
            return True
        else:
            self._hunger -= 5
            self._poop_on_floor += 0.5
            print(f"{self._name}: Yuck!!! It is not my favourite!")
            return False

    def drink(self, drink):
        while True:  # Based on favourite food of each robot.
            if drink == "lithium-ion" and self._model == "electric":
                self._thirst -= 15
                self._poop_on_floor += 0.5
                break
            elif drink == "oil" and self._model == "coal":
                self._thirst -= 15
                self._poop_on_floor += 0.5
                break
            elif drink == "steam" and self._model == "steam":
                self._thirst -= 15
                self._poop_on_floor += 0.5
                break
            elif (drink == "lithium-ion" or drink == "oil" or drink == "steam") \
                    and (self._model == "electric" or self._model == "coal"
                         or "steam"):
                self._thirst -= 5
                self._poop_on_floor += 0.5
                print(f"{self._name}: Eww!!! It is not my favourite drink!")
                break
            else:
                print()

    def clean(self, duster):
        while True:
            if (duster == "broom" or duster == "Broom") and self._poop_on_floor > 5:
                print(f"You clean up {self._name}.")
                self._poop_on_floor -= 5
                self._smell -= 25
                break
            elif (duster == "vacuum" or duster == "Vacuum") and self._poop_on_floor > 5:
                print(f"You clean up {self._name}.")
                self._poop_on_floor -= 10
                self._smell -= 45
                break
            else:
                print("There's nothing to clean.")
                break

    def bathe(self, brush):
        while True:
            if (brush == "sponge" or brush == "Sponge") and self._smell > 0:
                print(f"You bathe {self._name}.")
                self._smell -= 50
                self._poop_on_floor -= 50
                break
            elif (brush == "bathtub" or brush == "Bathtub") and self._smell > 0:
                print(f"You bathe {self._name}.")
                self._smell = 0
                self._poop_on_floor = 0
                break
            else:
                print(f"{self._name} is already clean.")
                break

    def sleep(self):
        while True:
            if 0 < self._energy < 100:
                print(f"{self._name} is sleeping.")
                self._energy += 25
                time.sleep(5)
            else:
                print(f"{self._name} is feeling energetic!")
                break

    def dance(self):
        print(f"{self._name} perform a robot break-dance.")

    def play(self):
        if self._loneliness == 100:
            print(f"{self._name} isn't in the mood to play...")
            return
        elif self._hunger > 60:
            print(f"{self._name} is too hungry to play!")
            return
        elif self._thirst > 60:
            print(f"{self._name} is too thirsty to play!")
            return

        else:
            print(f"You throw the ball for {self._name} to fetch.")
            if self._happiness >= 80:
                print(f"{self._name} retrieves the ball with lightning speed!")
                self._smell += 5
            elif self._happiness >= 70:
                print(f"{self._name} takes their time retrieving the ball.")
                self._smell += 5
            else:
                print(
                    f"{self._name} watches the ball fall and looks at you dumbly.")
            self._hunger += 20
            self._energy -= 20

    def heal(self):
        if self._health < 100:
            print(f"You heal up {self._name}.")
            self._health += 15
            print(f"{self._name} is healed now.")

        else:
            print(f"{self._name} is not sick.")

    def chitchat(self, event="droid"):  # Expression states.
        faces = {
            "droid": "(๑>◡<๑)",
            "feed": "(๑´ڡ`๑)",
            "drink": "(๑´ڡ`๑)",
            "play": "(ฅ^ω^ฅ)",
            "sleep": "୧(๑•̀⌄•́๑)૭✧",
            "shower": "( •̀ .̫ •́ )✧"
        }

        talks = {
            "droid": "Hi {}, my name is {}. I am a {} model of {} robot.".format(self._owner, self._name,
                                                                                 self._gender, self._model),

            "feed": "Yummy!",
            "drink": "Tasty drink ~",
            "play": "Happy to have your company ~",
            "sleep": "What a beautiful day!",
            "shower": "Thanks ~"
        }

        s = "{} ".format(faces[event]) + ": " + talks[event]
        print(s)

    def status(self):
        print("Hunger:")
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

        print("Thirst:")
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
            print(f"{self._name} is no more...")


def main():
    print("Welcome to Gothie's virtual pet robot! You will have the opportunity to raise a robot.")
    print("Let's head to the pet creation process.\n")
    owner = str(input("Please enter your name: "))
    answer = str(input(f"Are you okay with {owner.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer == "Y" or answer == "y":
            owner = owner.capitalize()
            break

        else:
            owner = input("Please enter your name: ")
            answer = str(input(f"Are you okay with {owner.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))

    print(f"Dear {owner}, we will create your pet robot!")
    name = str(input("How will you name your pet: "))
    answer1 = str(input(f"Are you okay with {name.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer1 == "Y" or answer1 == "y":
            name = name.capitalize()
            break

        else:
            name = input("Please enter your pet's name: ")
            answer1 = str(input(f"Are you okay with {name.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))

    gender = str(input("What is your pet's gender?\nPress \"M\" for male or \"F\" for female: "))
    answer2 = str(input(f"Are you okay with {gender.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer2 == "Y" or answer2 == "y":
            if gender == "M" or gender == "m":
                gender = "male"
                pp = "he"
                pop = "his"
                break

            elif gender == "F" or gender == "f":
                gender = "female"
                pp = "she"
                pop = "her"
                break
        else:
            gender = input("Please enter your pet's gender: ")
            answer2 = str(input(f"Are you okay with {gender.capitalize()}?\nPress \"Y\" for yes or \"N\" for no."))

    model = str(input("What is your pet's type, \"electric\", \"coal\" or \"steam\": "))
    answer3 = str(input(f"Are you okay with {model}?\nPress \"Y\" for yes or \"N\" for no."))
    while True:
        if answer3 == "Y" or answer3 == "y":
            if model == "Electric" or model == "electric":
                model = "electric"
                break

            elif model == "Coal" or model == "coal":
                model = "coal"
                break

            elif model == "Steam" or model == "steam":
                model = "steam"
                break
        else:
            model = input(
                "Please enter your pet's type. You can choose between \"electric\", \"coal\" or \"steam\": ")
            answer3 = str(input(f"Are you okay with {model}?\nPress \"Y\" for yes or \"N\" for no."))

    print("Processing.")
    time.sleep(1)
    print("Processing..")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    age = 0
    bot = Droid(owner, name, gender, model, age)

    #  def game(self):
    print(bot.stats())
    print(textwrap.dedent("""_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._."""))
    print(
        f"Pet sheet: [{name}]: {pp.capitalize()} is the {gender} {model.lower()} type and {pop} caregiver is {owner}"
        f".")
    print(textwrap.dedent("""_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._."""))
    print(
        f"\n{name}: Greetings, {owner}! I am happy to see you!\nI can eat, drink, shower, sleep, or play with you if "
        f"you enter each of the following commands:\n")
    print(textwrap.dedent("""
    #----------------MENU--------------#
    # \"F\" for [feed], \"D\" for [drink]  #
    # \"C\" for [clean], \"B\" for [bath]  #
    # \"Z\" for [sleep], \"P\" for [play]  #
    # \"X\" for [heal], \"O\" for  [chat]  #
    # You can check my status with: \"H\"#
    # For [status], press \"Q\" to quit: #
    #----------------------------------#
    """))
    prompt = input()

    if prompt == "F" or prompt == "f":
        food = input("Please choose between \"lightning bolt\", \"coal\" or \"ice\":")
        while not bot.feed(food):
            food = input("Please choose between \"lightning bolt\", \"coal\" or \"ice\":")

    elif prompt == "D" or prompt == "d":
        drink = input("Please choose between \"lithium-ion\", \"oil\" or \"steam\":")
        while not bot.drink(drink):
            drink = input("Please choose between \"lithium-ion\", \"oil\" or \"steam\":")

    elif prompt == "C" or prompt == "c":
        duster = input("Please choose between a \"broom\" or a  \"vacuum\" cleaner:")
        while not bot.clean(duster):
            duster = input("Please choose between a \"broom\" or a  \"vacuum\" cleaner:")

    elif prompt == "B" or prompt == "b":
        brush = input("Please choose between a \"sponge\" bath or a  \"bathtub\" bath:")
        while not bot.clean(brush):
            brush = input("Please choose between a \"sponge\" bath or a  \"bathtub\" bath:")

    elif prompt == "Z" or prompt == "z":
        bot.sleep()

    elif prompt == "P" or prompt == "p":
        bot.play()

    elif prompt == "X" or prompt == "x":
        bot.heal()

    elif prompt == "O" or prompt == "o":
        bot.chitchat()

    elif prompt == "H" or prompt == "h":
        print(bot.status())


if __name__ == "__main__":
    main()