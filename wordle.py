import os
os.system('clear')

BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"

print('WORDLE')

correct = 'SHAKE'

guess = input('Please guess. > ').upper()

#Check EACH Letter
for i in range(0, 5):
  if guess[i] == correct[i]:
    print(f"{BG_GREEN}{guess[i]}{RESET}", end="")
  elif guess[i] in correct:
    print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
  else:
    print(guess[i], end="")

print()
