import random

number = random.randint(1, 10)
tries = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != number:
    tries += 1
    guess = input(f'Enter guess #{tries}: ')

    if guess == 'quit': 
        break
    
    if guess.isnumeric() == False:
        print('Numbers only, please!')
        continue
    guess = int(guess)

    if guess < number:
        print('Your guess is too low, try again!')
    if guess > number:
        print('Your guess is too high, try again!')

else:
    print(f'You guessed it in {tries} tries!')
