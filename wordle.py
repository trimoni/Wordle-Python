import os
os.system('clear')

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

