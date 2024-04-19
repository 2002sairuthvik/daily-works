# About Random
import random
random_int = random.random()
print(random_int)
import random
toss = random.randint(0,1)
if toss==1:
  print("Heads")
else :
  print("Tails")


# lists data type
states_of_america = ["Delaware", "Pennsylvania", "New Jersey","Georgia", "Connecticut", "Massachusetts", "Maryland"]
print(states_of_america[-1])

# Exercise below

names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
name_choose = random.randint(0,len(names)-1)
print(f'{names[name_choose]} is going to buy the meal today!')

# Nested-Lists
fruits = ["Strawberries","Apples","Oranges","Watermelon","Grapes","Peaches"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
combined = [fruits,vegetables]
print(combined)

# Exercise below
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a","b","c"]
num = int(position[1])-1
all = abc.index(letter)
map[num][all] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

# rock paper nd scissors exercise
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random
print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice>=3 or player_choice<0:
  print("You typed an invalid number, you lose!")
else :
  if player_choice == 0:
    print(rock)
  elif player_choice == 1:
    print(paper)
  elif player_choice == 2:
    print(scissors)

  print("Computer chose:")
  computer_choice = random.randint(0, 2)
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  elif computer_choice == 2:
    print(scissors)

  if player_choice == 0 and computer_choice == 0:
    print("It's a draw!")
  elif player_choice == 0 and computer_choice == 1:
    print("You lose!")

  elif player_choice == 0 and computer_choice == 2:
    print("You win!")
  elif player_choice == 1 and computer_choice == 0:
    print("You win!")
  elif player_choice == 1 and computer_choice == 1:
    print("It's a draw!")
  elif player_choice == 1 and computer_choice == 2:
    print("You lose!")
  elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
  elif player_choice == 2 and computer_choice == 1:
    print("You win!")
  elif player_choice == 2 and computer_choice == 2:
    print("It's a draw!")

