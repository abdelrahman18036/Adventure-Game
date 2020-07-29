import time
import random

items = []

Weapon = ['M4A1', 'M700', 'MG3', 'M16', 'Sword', 'dagger']
Monster = ['Pirate', 'Dragon', 'Gorgen', 'troll']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("Welcome in the game!")
    name = input("What is your name ?\n")
    if not name:
        return intro()
    else:
        return intro2(name)


def intro2(name):
    Weapon_of_game = random.choice(Weapon)
    Monster_of_game = random.choice(Monster)
    items.clear()
    print_pause("{}, You find yourself standing in the open field,"
                " filled with grass and yellow wildflowers.".format(name))
    print_pause("Rumor has it that {} a wicked fairie is somewhere"
                "around here, and has  been terrifying "
                "the nearby village.".format(Monster_of_game))
    print_pause("In front of you is the house.\n"
                "To your right is a dark cave.")
    print_pause("In your hand you hold your tursty "
                "(but not very effective) {}.".format(Weapon_of_game))
    place_choice(name, Weapon_of_game, Monster_of_game)


def first_choice(name, Weapon_of_game, Monster_of_game):
    print_pause("\n{}, You knock on the door of the house.".format(name))
    print_pause("You approach the  door of the house.")
    print_pause("You are about to knock when"
                "the door opens and out steps a {}.".format(Monster_of_game))
    print_pause("Eep! This is the {}'s house!".format(Monster_of_game))
    print_pause("The {} attacks you!".format(Monster_of_game))
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a {}.".format(Weapon_of_game))
    fight_choice(name, Weapon_of_game, Monster_of_game)


def second_choice(name, Weapon_of_game, Monster_of_game):
    print_pause("\n{}, You peer into the cave.".format(name))
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of magic material behind a rock.")
    print_pause("You have found if you use it in your {}"
                " ,it will make the weapon"
                " more strong!".format(Weapon_of_game))
    print_pause("You put it on the  your {}".format(Weapon_of_game))
    print_pause("You walk back out to the field.")
    items.append(Weapon_of_game)
    place_choice(name, Weapon_of_game, Monster_of_game)


def fight_choice(name, Weapon_of_game, Monster_of_game):
    fight_or_not = input("\nWould you like to (1) fight or (2) "
                         "go back to the choices?\n")
    if fight_or_not == '1':
        print_pause("The {}  shines brightly in your hand "
                    "as you brace yourself for the attack."
                    .format(Weapon_of_game))
        print_pause("But the {} takes one look at your shiny"
                    "new toy and runs away!".format(Monster_of_game))
        print_pause("You have rid the town of the {}."
                    "You are victorious!".format(Monster_of_game))
        print_pause("well done! , You win")
        play_again(name)
    elif fight_or_not == '2':
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        place_choice(name, Weapon_of_game, Monster_of_game)
    else:
        print_pause("Please {}, enter 1 or 2!\n".format(name))
        fight_choice(name, Weapon_of_game, Monster_of_game)


def place_choice(name, Weapon_of_game, Monster_of_game):
    print_pause("\nIn front of you are two choices.\n")
    choice = input("Enter 1 knock on the door of the house.\n"
                   "Enter 2 peer into the cave.\n"
                   "What choice do you want to do ?\n")
    if choice == '1':
        first_choice(name, Weapon_of_game, Monster_of_game)
    elif choice == '2':
        second_choice(name, Weapon_of_game, Monster_of_game)
    else:
        print_pause("Please {}, enter 1 or 2!\n".format(name))
        place_choice(name, Weapon_of_game, Monster_of_game)


def play_again(name):
    choice_again = input("\nWould you like to play again ?"
                         " Please say 'yes' or 'no'.\n").lower()
    if 'no' in choice_again:
        print_pause("\nOk, Goodbye {}.".format(name))

    elif 'yes' in choice_again:
        print_pause("\nExcellent {}, restarting the game ...".format(name))
        intro2(name)
    else:
        print_pause("Please {}, enter 'yes' or 'no'!".format(name))
        play_again(name)


intro()
