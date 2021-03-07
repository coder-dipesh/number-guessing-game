# Number guessing game between two player.

player1 = input('Please enter your name as Player 1: ')
player2 = input('Please enter your name as Player 2: ')
print('\n')
secret_number = int(input(f'Enter a secret number to guess by {player2}: '))
guess_limit = int(
    input(f'Enter the number of maximum guesses you want to allow {player2}: '))
guess_count = 0

while guess_count < guess_limit:
    guess = int(input(f'Guess the number entered by {player1} : '))
    guess_count += 1
    if guess == secret_number:
        print('Hurrey!! You Won!')
        break  # To end loop
else:
    print('Oops! You made three guesses but failed!')
