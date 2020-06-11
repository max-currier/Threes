from sys import exit
import random

def start():
    print("""
    This is a the classic dice game of Threes (v1.1).

    Players start with 5 dice and roll them all to start the game.
    After each roll, the player must pull at least one die.
    That die contributes to their score and is removed and can no longer be rolled.
    Roll and pull die until no dice remain. Threes count for zero points.
    The player with the lowest score wins.

    If you select multiple die per turn, you MUST separate them by SPACES.
    e.g. "3 3 1"

    Players cannot "double down" in this version...yet.

    Press crtl+c to quit at any time
    """)
    in_play = 5 # number of dice to start game
    in_hand = [] # empty list to store dice selected by player
    hand_total = 0 # establishing starting score of zero

    # double-down feature not yet built in, but i entered it here as a framework
    # of to track it, passing a T/F value from fn to fn and building in a
    # conditional statement in the choose() fn to test if player an dd
    double_down = True # start game off with ability to double down once, or until this is False

    roll_dice(in_play, in_hand, hand_total, double_down)


def roll_dice(in_play, in_hand, hand_total, double_down): # function to determine dice roll
    roll = []

    for i in range(in_play): #this is the RNG for dice roll
        die = random.randint(1, 6)
        roll.append(die)

    print(f"You rolled {roll}.\n")

    choose(in_play, in_hand, hand_total, double_down, roll)


def choose(in_play, in_hand, hand_total, double_down, roll): #function that allows player to choose dice
        keep_list = [int(item) for item in input("Enter values of die you would like to keep, separated by spaces.\n>>>").split()]

        for val in keep_list:
            if val in roll:
                pass

            else:
                print(f"\nYour selections must be from your last roll, {roll}\n")

                choose(in_play, in_hand, hand_total, double_down, roll)

        for val in keep_list: # had to append val AFTER input test to avoid double-counting incorrectly entered vals
            if val in roll:
                in_hand.append(val)

        in_play -= len(keep_list) # removing number of selections from num of dice left to roll
        hand_total = sum(in_hand)

        for i in in_hand:
            if i == 3:
                hand_total -=3

        if in_play > 0:
            print(f"\nYou now have {in_hand} in your hand, for a total score of {hand_total}.")
            print("Time to roll again! \n")

            roll_dice(in_play, in_hand, hand_total, double_down)

        else:
            end(in_hand, hand_total)


def end(in_hand, hand_total): # function that displays final score after all dice have been chosen
    print(f"Your now have {in_hand} in your hand, \nfor a FINAL SCORE of {hand_total}.")


start()
