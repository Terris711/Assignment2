import time
from random import randint
import matplotlib.pyplot as plt

from human import Human
from vampire import Vampire
from items import *


def graph(humans, vampires, items):

    # plt.clf()
    for human in humans:
        plt.plot(human.location[0], human.location[1], "ro")

    for vampire in vampires:
        plt.plot(vampire.location[0], vampire.location[1], 'ko')

    for item in items:
        if item.itemTypes == "water":
            plt.plot(item.location[0], item.location[1], 'bv')

        elif item.itemTypes == "food":
            plt.plot(item.location[0], item.location[1], 'ms')

        elif item.itemTypes == "garlic":
            plt.plot(item.location[0], item.location[1], 'y*')

    plt.show(block=False)
    plt.pause(1)
    plt.clf()


def isInteracting(location1, location2):
    if abs(location1[0] - location2[0]) <= 1 and abs(location1[1] - location2[1] <= 1):
        return True
    else:
        return False


number_of_humans = int(input("Enter initial number of humans: "))
number_of_vampires = int(input("Enter initial number of vampires: "))
timestep = int(input("Enter time step: "))


number_of_items = randint(0,100)

humans = []
vampires = []
items = []

arrayTypeOfItem = ["water", "food", "garlic"]


for i in range(number_of_humans):
    if (i == 0):
        humans.append(Human())
    else:
        # humans.append(Human(humans))
        human = Human(humans)
        humans.append(human)

for i in range(number_of_vampires):
    if (i == 0):
        vampires.append(Vampire(humans))
    else:
        vampires.append(Vampire(humans, vampires))

for i in range(number_of_items):
    index = randint(0,2)
    items.append(Items(arrayTypeOfItem[index]))


for i in range(timestep):

    # Humans do not interact
    for human in humans:
        # If human do not move anymore => human disappear
        if human.moving() == False:
            humans.remove(human)
        else:
            human.interact = False

    # vampire do not interact
    for vampire in vampires:
        vampire.interact = False
        vampire.moving()

    # Humans interact with vampire and food, water, garlic
    for human in humans:
        if human.interact == True:
            continue

        # check surroundings

        # check whether or not humans are here
        for human2 in humans:
            if isInteracting(human.location, human2.location):
                probability = randint(0, 100)
                if probability <= 40:
                    # attack
                    human.human_attack()
                    human2.human_attacked()
                    print("Human attacked each other!")
                else:
                    # help each other
                    human.human_help()
                    human2.human_help()
                    print("Human helped each other!")

        # check whether or not vampires are here
        for vampire in vampires:
            if isInteracting(human.location, vampire.location):
                probability = randint(0, 100)
                if probability <= 70:
                    # human is infected
                    vampires.append(Vampire(human.health))
                    humans.remove(human)
                    print("Human is infected!")
                    break
                else:
                    # vampire is killed by human
                    vampires.remove(vampire)
                    print("Vampire is killed by human!")

        # check the interaction between human and items
        for item in items:
            if isInteracting(human.location, item.location):
                if item.itemTypes == "water":
                    human.health += 50
                    print("Human have just drunk water!")
                elif item.itemTypes == "food":
                    human.health += 30
                    print("Human have just eaten food!")
                elif item.itemTypes == "garlic":
                    human.health += 100
                    print("Human have just used garlic!")

    graph(humans, vampires, items)
    time.sleep(1)
    if i >= timestep-1:
        input("Press Enter to continue...")
