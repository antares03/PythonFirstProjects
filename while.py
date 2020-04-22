number = 23
running = True

while running:
    guess = int(input('enter a integer : '))

    if guess == number:
        print('Congratulations, you guessed right!')
        running = False # this stops the while loop
    elif guess < number:
        print('No, the number guessed is a bit more than that')
    else:
        print('No, the number guessed is a little less than that')
else:
    print('While loop is finished.')
    # In this area you can enter all you need

print('Completion')
