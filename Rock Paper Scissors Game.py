# Rock Paper Scissors ASCII Art

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random
game_images= [Rock, Paper, Scissors]

End_game=False
while not End_game:
 print("=====Rock Paper Scissors: The Python Game=====")
 print("\n")

#Input form user
 user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n =>"))
 if user_choice>=3 or user_choice<0:
  print("you have entered an invalid choice. Choose again !!!")
 else:
  print("You Choose: ")
  print(game_images[user_choice])
  #computer choice
  computer_choice=random.randint(0,2)
  print("Computer choose: ")
  print(game_images[computer_choice])

  #rules & logics 
  
  if user_choice==2 and computer_choice==0:
   print("You lose !!!")
  elif user_choice > computer_choice :
   print("You win")
  elif user_choice==0 and computer_choice==2 :
   print("You Win !!!")
  elif user_choice < computer_choice:
   print("You lose !!!")
  elif user_choice==0 and computer_choice==1 :
   print("You lose !!!")
  elif user_choice==computer_choice:
   print("It's a draw !!")
 exit = input("DO you want to exit this game !! type Y for yes and N for no \n =>").lower()    #exit the game
 if exit=="y" :
  End_game=True
  print("\n Thank you for playing Rock paper scissor game !!!\n ")
 elif exit=="n":
  print("\n Continue with the game !!\n")
 else:
  print("\n As you have entered the invalid choice game continues \n")
  
