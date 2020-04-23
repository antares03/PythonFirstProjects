number = 23
guess = int(input('Input integer number : '))

if guess == number:
    print('Congratulations, you guessed it!') # Здесь начинается новый блок
    print('But you do not win any prizes') # Здесь заканчивается новый блок
elif guess < number:
    print('No, it is a little higher than that') # Ещё один блок
    # Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('No, it is a little lower than that')
    # чтобы попасть сюда, guess должно быть больше, чем number

print('Done')
# Это последнее выражение выполняется всегда после выполнения оператора if
