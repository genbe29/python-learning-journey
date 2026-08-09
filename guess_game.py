player1 = int(input('Player 1, choose a number from 1 to 10: '))

print('Player 2, you have 3 attempts to guess the number 🎲')

for i in range(3):
    player2 = int(input('Enter number: '))

    if player2 == player1:
        print("You're right🎉")
        break

    elif player2 > player1:
        print('Too high, try lower number ⬇️')

    else:
        print('Too low, try a higher number ⬆️')
