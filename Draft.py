#  Importing food and drinks from consumable. Summoning random for starting values.
from venv.game.consumable import ElectricBotFood
from venv.game.consumable import CoalBotFood
from venv.game.consumable import SteamBotFood
from venv.game.consumable import Water
from venv.game.consumable import Oil
from venv.game.consumable import LiIon
from random import randint

#  import json
# import pickle

# player = Player(...)
# level_state = Level(...)

# saving
# with open('savefile.dat', 'wb') as f:
#    pickle.dump([player, level_state], f, protocol=2)

# loading
# with open('savefile.dat', 'rb') as f:
#    player, level_state = pickle.load(f)


# Min and Max values along with food and drinks values for each bot.
MIN, MAX = 0, 10
electric_edible_items = [ElectricBotFood]
coal_edible_items = [CoalBotFood]
steam_edible_items = [SteamBotFood]
electric_drinkable_items = [LiIon]
coal_drinkable_items = [Oil]
steam_drinkable_items = [Water]


#  electric_icon = ["/icons/Spark.png"]
#  coal_icon = ["/icons/Flame.png"]
#  steam_icon = ["/icons/Steam.png"]


#  Defining Droid class.
class Droid(object):  # Initialising values to defaults.
    def __init__(self, owner="Erisa", name="Gothie", gender="Female", model="Electric"):
        self._owner = owner.capitalize()
        self._name = name.capitalize()
        self._gender = gender
        self._model = model
        self._edible_items = []  # Food list. Defined top of here.
        self._drinkable_items = []  # Drink list. Defined top of here.
        #   self._phrases = []  # Chatterbot. WIP.

        #   self._age = 0  # Increment each day. WIP.
        #   self._weight = 0.5  # Increases if full. WIP.
        self._hunger = randint(0, 5)  # Random value between 0 and 50 percent.
        self._thirst = randint(0, 5)  # Same as above.
        self._smell = randint(0, 5)  # Same as above.
        self._loneliness = randint(0, 5)  # Same as above.
        self._energy = randint(5, 10)  # Random value between 50 to 100.
        #    self._illness = "None"  # Illness state.
        #    self._hp = 100  # HP for adventure mode.

        self._reply_to_master("newborn")
        self._update_status()

    def _time_pass_by(self, t=1):  # Time elapsed. t = 1 sec it seems.
        self._hunger = min(MAX, self._hunger + (0.2 * t))  # Minimum value between Max value and New hunger value.
        self._thirst = min(MAX, self._thirst + (0.2 * t))  # Same as above.
        self._smell = min(MAX, self._smell + (0.1 * t))  # Same as above.
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))  # Same as above.
        self._energy = max(MIN, self._energy - (0.2 * t))  # Maximum value between Min value and new energy value.

    def get_hunger_level(self):  # Return hunger level.
        return self._hunger

    def get_thirst_level(self):  # Return thirst level.
        return self._thirst

    def get_energy_level(self):  # Return energy level.
        return self._energy

    def shower(self):  # Determine cleanliness after bath.
        time = 4  # It takes 4 secs.
        self._time_pass_by(time)

        self._smell = 0
        self._loneliness = max(MIN, self._loneliness - time)

        self._reply_to_master("shower")
        self._update_status()

    def sleep(self):  # Determine sleepiness after sleeping.
        time = 7  # It takes 7 secs.
        self._time_pass_by(time)

        self._energy = min(MAX, self._energy + time)

        self._reply_to_master("sleep")
        self._update_status()

    def play_with(self):  # Determine sleepiness after playing.
        time = 4  # It takes 4 secs.
        self._time_pass_by(time)

        self._energy = max(MIN, self._energy - time)
        self._loneliness = max(MIN, self._loneliness - time)
        self._smell = min(MAX, self._smell + time)

        self._reply_to_master("play")
        self._update_status()

    def drink(self, liquid):  # Determine if thirsty or not.
        if isinstance(liquid, tuple(self._drinkable_items)):  # Checks if liquid is the type listed in drinks class.
            #  Drinks is listed as tuple. It will be true if liquid is in a tuple of drinks class, like water.
            #  Drinkable is defined at the top of this.

            self._time_pass_by()

            if self._thirst >= liquid.get_quantity():
                self._thirst = self._thirst - liquid.get_quantity()

            elif self._thirst <= 0:
                print("Too much drink to finish. I will leave some for you.")

            else:
                self._thirst = 0
        else:
            print("Not drinkable")

        self._reply_to_master(event="drink")
        self._update_status()

    def feed(self, food):  # Determine if thirsty or not.
        if isinstance(food, tuple(self._edible_items)):  # Checks if food is the type listed in consumable class.
            #  Food is listed as tuple. It will be true if food is in a tuple of food class, like chocolate.
            #  Edible is defined at the top of this.

            self._time_pass_by()

            if self.get_hunger_level() >= 2:

                if self._hunger >= food.get_quantity():
                    self._hunger = self._hunger - food.get_quantity()

                elif self._hunger <= 0:
                    print("Too much feed to finish. I will leave some for you.")

                else:
                    self._hunger = 0

                self._reply_to_master(event="feed")

            else:
                print("Your pet is satisfied, no desire for sustenance now.")

        else:
            print("Not edible")

        self._update_status()

    def _reply_to_master(self, event="newborn"):  # Expression states.
        faces = {
            "newborn": "(๑>◡<๑)",
            "feed": "(๑´ڡ`๑)",
            "drink": "(๑´ڡ`๑)",
            "play": "(ฅ^ω^ฅ)",
            "sleep": "୧(๑•̀⌄•́๑)૭✧",
            "shower": "( •̀ .̫ •́ )✧"
        }

        talks = {
            "newborn": "Hi {}, my name is {}. I am a {} model of {} robot.".format(self._owner, self._name,
                                                                                   self._gender, self._model),

            "feed": "Yummy!",
            "drink": "Tasty drink ~",
            "play": "Happy to have your company ~",
            "sleep": "What a beautiful day!",
            "shower": "Thanks ~"
        }

        s = "{} ".format(faces[event]) + ": " + talks[event]  # NO PRINT?
        print(s)

    def show_status(self):  # Show statuses.
        list_show = [
            ["Energy", self._energy],
            ["Hunger", self._hunger],
            ["Loneliness", self._loneliness],
            ["Smell", self._smell],
            ["Thirst", self._thirst]
        ]

        list_show.sort()

        for show in list_show:
            print("{:<12s}: [{:<20s}]".format(show[0], 2 * round(show[1]) * "#") + "{:5.2f}/{:2d}".format(show[1], 10))

    def _update_status(self):
        pass


#    def _update_status(self):
#        faces = {
#            "default": "(๑>◡<๑)",
#            "hunger": "(｡>﹏<｡)",
#            "thirst": "(｡>﹏<｡)",
#            "energy": "(～﹃～)~zZ",
#            "loneliness": "(〃∀〃)",
#            "smell": "(⁰▿⁰)"
#        }

#       talks = {
#           "default": "I feel good.",
#           "hunger": "I am so hungry ~",
#           "thirst": "Could you give me some drinks? Alcohol-free please ~",
#           "energy": "I really need to get some sleep.",
#           "loneliness": "Could you stay with me for a little while ?",
#           "smell": "I am sweaty"
#       }


class ElectricBot(Droid):  # Adding Electric bot model from Droid class.
    def __init__(self, owner="Erisa", name="Gothie", gender="Female", model="Electric"):
        Droid.__init__(self, owner, name, gender, model)
        self._edible_items = electric_edible_items
        self._drinkable_items = electric_drinkable_items


class CoalBot(Droid):  # Adding Coal bot model from Droid class.
    def __init__(self, owner="Erisa", name="Gothie", gender="Female", model="Coal"):
        Droid.__init__(self, owner, name, gender, model)
        self._edible_items = coal_edible_items
        self._drinkable_items = coal_drinkable_items


class SteamBot(Droid):  # Adding Steam bot model from Droid class.
    def __init__(self, owner="Erisa", name="Gothie", gender="Female", model="Electric"):
        Droid.__init__(self, owner, name, gender, model)
        self._edible_items = steam_edible_items
        self._drinkable_items = steam_drinkable_items


def main():
    global Droid
    print("Welcome to Gothie's pet robot game!")
    while True:  # Asking user input.
        prompt = input("Please input your name, the pet's name, gender(Male, Female), model(Electric, Coal or Steam), "
                       "separated by space.\nExample: [Erisa] [gothie] [female] [electrical]\n(Hit Enter to use "
                       "default settings): ")
        if prompt == "":
            Droid = ElectricBot()
            break

        if prompt != "":
            prompt_list = prompt.split()
            if prompt_list[2] == "male" or prompt_list[2] == "female":
                if prompt_list[3] == "coal":  # Gender.
                    Droid = CoalBot(prompt_list[0], prompt_list[1], prompt_list[2],
                                    prompt_list[3])
                    break

                elif prompt_list[3] == "steam":
                    Droid = SteamBot(prompt_list[0], prompt_list[1], prompt_list[2], prompt_list[3])
                    break

                elif prompt_list[3] == "electric":
                    Droid = ElectricBot(prompt_list[0], prompt_list[1], prompt_list[2], prompt_list[3])
                    break

                else:
                    continue
            else:
                continue

    intro = "\nI can eat, drink, shower, sleep, or play with you if you enter each of the following commands:\n" \
            "--- [feed] [drink] [shower] [sleep] [play]\n" \
            "You can also check my health status by entering:\n" \
            "--- [status]."
    print(intro)

    prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")

    true_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # Quantity.
    while prompt.lower() != "q":

        if prompt == "feed":

            while True:

                quantity = input("How much food ? 1 - 10 scale: ")
                if quantity in true_list:
                    quantity = int(quantity)
                    break
                else:
                    print("Invalid input.")

            if type(Droid) == ElectricBot:
                Droid.feed(ElectricBotFood(quantity))
            if type(Droid) == CoalBot:
                Droid.feed(CoalBotFood(quantity))
            if type(Droid) == SteamBot:
                Droid.feed(SteamBotFood(quantity))

        elif prompt == "drink":

            while True:

                quantity = input("How much drink ? 1 - 10 scale: ")
                if quantity in true_list:
                    quantity = int(quantity)
                    break
                else:
                    print("Invalid input.")

            Droid.drink(Water(quantity))

        elif prompt == "shower":
            Droid.shower()

        elif prompt == "sleep":
            Droid.sleep()

        elif prompt == "play":
            Droid.play_with()

        elif prompt == "status":
            Droid.show_status()

        elif Droid.get_energy_level() >= 10:
            print("Your pet is too energetic to fall sleep.")

        else:
            print("Invalid command.")

        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")

    print("Bye ~")


# just the main
if __name__ == "__main__":
    main()
