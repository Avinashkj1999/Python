from random import randint

EASY_LEVEL_RETURN=10
HARD_LEVEL_RETURN=5

def Check_answer(guess, answer,turns):
 if guess > answer:
  print("Too high")
  return turns-1
 elif guess < answer:
  print("too low")
  return turns-1
 else:
  print(f"you guess the correct number, i was thinking about {answer}")

def check_level():
 level=input("Easy or Hard: ").lower()
 if level== "easy":
  return EASY_LEVEL_RETURN
 elif level=="hard":
  return HARD_LEVEL_RETURN



def game():
 print("Welcome to guess the number game")
 print("Thinking of a number between 1 to 100 /\/\/\/")
 
 answer=randint(1,100)

 turns=check_level()
 
 while turns >=0:
  print(f"You have {turns} attempt remaining to guess the number")
  
  guess=int(input("Guess the number i'm thinking: "))
  
  turns=Check_answer(guess,answer,turns)
  if turns==0:
   print("you've runout of guess, you lose !!")
   return
  elif turns!= 0:
   print("Guess again")

game()