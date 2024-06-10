"""
Mad Lib-type Project
By Kate Tuscano
A Mad Lib school project."""

# import statements

import os

# Welcome the user
print("Welcome! This program will ask you for various words to fill in a story.")

# Get user input

place = input("Enter a place: ")
place_2 = input("Enter another place: ")

verb = input("Enter a verb: ")
verb_2 = input("Enter another verb: ")
verb_3 = input("Enter another verb: ")
verb_4 = input("Enter a past tense verb: ")

adjective = input("Enter an adjective that ends with -ly: ")
adjective_2 = input("Enter another adjective that ends with -ly: ")
adjective_3 = input("Enter another adjective: ")
adjective_4 = input("Enter another adjective: ")

body_part = input("Enter a body part: ")

# Build story

def print_story():
    print("     A Dog and a Cock, who were the best of friends, wished very much to see something of the world. So they decided to leave the " + place)

    print("and to set out into the world along the road that led to the " + place_2 + ". The two comrades traveled along in the very best of spirits and")
          
    print(" without meeting any adventure to speak of.")

    print("     At nightfall the Cock, looking for a place to " + verb_3 + ", as was his custom, spied nearby a hollow tree that he thought would do very")
    
    print(" nicely for a night's lodging. The Dog could " + verb + " inside and the Cock would fly up on one of the branches. So said, so done, and both slept ")

    print(" very " + adjective + ". With the first glimmer of dawn the Cock awoke.")

    print("     For the moment he forgot just where he was. He thought he was still in the " + place + " where it had been his duty to " + verb_2 + " the household at daybreak.")
    
    print("So standing on tip-toes he flapped his wings and crowed " + adjective_2 + ". But instead of awakening the farmer, he awakened a Fox not far off in the wood. The Fox immediately had")

    print(adjective_3 + " visions of a very delicious breakfast. Hurrying to the tree where the Cock was " + verb_3 + "ing, he said very politely: A hearty welcome to our " + place_2 + ",")

    print("honored sir. I cannot tell you how glad I am to see you here. I am quite sure we shall become the closest of friends. I feel highly flattered, kind sir, replied the Cock slyly.")

    print("If you will please go around to the door of my house at the " + body_part + " of the tree, my porter will let you in. The " + adjective_4 + " but unsuspecting Fox, went around the tree")

    print("as he was told, and in a twinkling the Dog had " + verb_4 + " him.")

# Display results

enter = input("Press enter to display story: ")

os.system('cls')
print_story()

# Thank the user and quit

print(" ")
print("Thanks for playing!")