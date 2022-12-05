import os
os.system('clear')

BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

print('WORDLE')

correct = 'SHAKE'

guess = input('Please guess. > ').upper()

#Check First Letter

if guess[0] == correct[0]:
  print(f"{BG_GREEN}{guess[0]}{RESET}")
elif guess[0] in correct:
  print(f"{BG_YELLOW}{guess[0]}{RESET}")
else:
  print(guess[0])

