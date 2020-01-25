# TASK C
# a) Create a function that takes a name and returns a greeting.
# hello_name("Gerald") ➞ "Hello Gerald!"


def hello_name(aname):
    greeting = "Hello" + " " + aname + "!"
    return greeting

print(hello_name("Gerald"))


# b. Write a function that takes the base and height of a triangle and return its area.
# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50


def area_tri(x,y):
    area = int(0.5 * x * y)
    return area

print(area_tri(3,2))
print(area_tri(7,4))
print(area_tri(10,10))


# c) Create a function that finds the maximum range of a triangles third edge.
# maximum range of third edge = (side1 + side2) - 1 .
# next_edge(8, 10) ➞ 17
# next_edge(5, 7) ➞ 11
# next_edge(9, 2) ➞ 10

def next_edge(x,y):
    max_range = int((x + y)-1)
    return max_range

print(next_edge(8,10))
print(next_edge(5,7))
print(next_edge(9,2))


# Create a function that takes a list and returns the first element.
# get_first_value([1, 2, 3]) ➞ 1
# get_first_value([80, 5, 100]) ➞ 80
# get_first_value([-500, 0, 50]) ➞ -500


def get_first_value(a,b,c):
    elements = [a,b,c]
    first_element = elements[0]
    return first_element

print(get_first_value(1,2,3))
print(get_first_value(80,5,100))
print(get_first_value(-500,0,50))


# i)Create a function that takes two strings as arguments and
# return either True or False
# depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
# comp("AB", "CD") ➞ True
# comp("ABC", "DE") ➞ False
# comp("hello", "edabit") ➞ False


def comp(string_one, string_two):

    length_of_string = len(string_one) or len(string_two)
    if len(string_one)==len(string_two):
        return(True)
    elif len(string_one)!=len(string_two):
        return(False)
    else:
        pass
    return length_of_string

print(comp("AB", "CD"))
print(comp("hello", "edabit"))
print (comp("ABC", "DE"))

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function







def list_of_numbers():
    initial_list = [5,10,15,20,25]
    derived_list = initial_list[0::4]
    print(derived_list)

list_of_numbers()
















# Abigail and Benson are playing Rock, Paper, Scissors.
# Each game is represented by an array of length 2,
# where the first element represents what Abigail played
# and the second element represents what Benson played.
# Given a sequence of games, determine who wins the most number of matches.
# If they tie, output "Tie".
# R stands for Rock
# P stands for Paper
# S stands for Scissors


import random

moves=("R","P","S")
loopcontrol=1

#Ask for the number of games to be played inorder to decide winner
best_of=int(input("Decide game after how many trials?"))

#Variables to capture the wins and ties of every individual
player_one_win_counter=0
player_two_win_counter=0
tie=0

#state of the game before anyone makes a move
game_state=[0,0]

#function to randomly generate a move for each player when called
def move():
    return random.choice(moves)

while loopcontrol<=best_of:



    game_state[0]=a=move() #Abigail Makes her Move
    game_state[1]=b=move() #Ben makes his move after Abigail

    print("Game State:",game_state) #Display their moves

    #check for wins and raws
    if game_state==['R','S'] or game_state==['P','R'] or game_state==['S','P']:
        player_one_win_counter+=1
        loopcontrol += 1
        print("Abigail Wins")

    elif game_state == ['R', 'P'] or game_state == ['P', 'S'] or game_state == ['S', 'R']:
        player_two_win_counter += 1
        loopcontrol += 1
        print("Ben Wins")

    else:
        tie+=1
        loopcontrol+=1
        print("It's a tie")

#Display overall Winners/Loosers/ Draws
if player_one_win_counter<player_two_win_counter:
    print("Ben is the Overall winner")
    print("Wins(",player_two_win_counter,":",player_one_win_counter,")")

elif player_one_win_counter>player_two_win_counter:
    print("Abigail is the overall Winner")
    print ( "Wins(", player_one_win_counter, ":", player_two_win_counter, ")" )
elif player_two_win_counter==player_one_win_counter:
    print("No winner, Ties")

print("Abigail:",player_one_win_counter)
print("Ben:",player_two_win_counter)
print("Ties:",tie)