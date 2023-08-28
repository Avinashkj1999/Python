print('''                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
      
       ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
  ''')

Stages=[
 '''  _______
 |/   |
 |   (_)
 |   \|/
 |    |
 |   / |
 |
 |___''',

 '''  _______
 |/   |
 |   (_)
 |   \|/
 |    |
 |   / 
 |
 |___''',
 
'''  _______
 |/   |
 |   (_)
 |   \|/
 |    |
 |    
 |
 |___''',
'''  _______
 |/   |
 |   (_)
 |   \|/
 |    
 |    
 |
 |___''',
'''  _______
 |/   |
 |   (_)
 |   \|
 |    
 |    
 |
 |___''',
 '''  _______
 |/   |
 |   (_)
 |    |
 |    
 |    
 |
 |___''',

 ''' _______
 |/   |
 |   (_)
 |    
 |    
 |    
 |
 |___'''
]
Stages[4]
import random

user_name=input("\nEnter your name \n")          #username input
print(f"\nHello {user_name}, start guessing letters \n")
 
list_of_words=["bruptly","absurd","abyss","foxglove","lucky","luxury","syndrome","subway"]   #list of words
choosen_word=random.choice(list_of_words)
word_length=len(choosen_word)
attempt=6

# print(choosen_word)       #fhide this line while playing this is jsut for testing 

display=[]

for _ in range(word_length):   #replace letters with blanks
  display+= "_"
print(display)

end_of_game=False
while not end_of_game:    #take iput form users
 guess=input("Guess a letter : ").lower()

 for position in range(word_length):     #update guess letter with display if guess letter is available in choosen word
  letter=choosen_word[position]
  if letter==guess:
   display[position]=letter
 if guess not in choosen_word:
  attempt-=1
  print(f"You loose a live\n {Stages[attempt]}")
  if attempt==0:
   end_of_game=True
   print("You Lose !!!! try your luck next time")
 print(f"{''.join(display)}")

 if "_" not in display:
   end_of_game=True
   print("Congratulation !!! You Win")
  