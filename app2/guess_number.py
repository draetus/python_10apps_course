import random

print('---------------------------------------------------')
print('             GUESS THAT NUMBER GAME')
print('---------------------------------------------------')
print()

number = random.randint(0,100)
guess = 'a'
name = input('Enter your name: ')

while guess != number:
    guess = int(input('Guess a number between 0 and 100: '))
    if guess < number:
         print('Sorry {1} .Your guess of {0} was too LOW'.format(guess, name))
    elif guess > number:
        print('Sorry {1} . Your guess of {0} was too high'.format(guess, name))
    else:
        print('YEAH The number was {0}, YOU WON {1}'.format(guess, name))
