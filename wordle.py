import os
os.system('clear')

BG_GREEN = "\u001b[42m"
BG_YELLOW 

print('WORDLE')

correct = 'SHAKE'

guess = input('Please guess. > ').upper()

print(guess)

#Check First Letter

if guess[0] == correct[0]:
  print('CORRECT')
elif guess[0] in correct:
  print('IN WORD and WRONG SPOT')
else:
  print('NOT IN WORD')

