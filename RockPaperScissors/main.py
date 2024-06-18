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

#Write your code below this line 👇
#Store the user's input:

users_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

#Definir as opções de escolha:

if users_choice == "0":
    print("You chose Rock")
    print(rock)
elif users_choice == "1":
    print("You chose Paper")
    print(paper)
elif users_choice == "2":
    print("You chose Scissors")
    print(scissors)
else:
    print("No available option")

#Definir a escolha do computador:
import random

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("I chose Rock")
    print(rock)
elif computer_choice == 1:
    print("I chose Paper")
    print(paper)
else:
    print("I chose Scissors")
    print(scissors)

#compare the user's and the computer's choice to determine the winner (or a draw).

if users_choice == "0" and computer_choice == 1:
    print("You lose")
elif users_choice == "0" and computer_choice == 2:
    print("You win")
elif users_choice == "1" and computer_choice == 0:
    print("You win")
elif users_choice == "1" and computer_choice == 2:
    print("You lose")
elif users_choice == "2" and computer_choice == 0:
    print("You lose")
elif users_choice == "2" and computer_choice == 1:
    print("You win")
else:
    print("It's a draw")
