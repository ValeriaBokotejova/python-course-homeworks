while True:
    user_input = int(input('Enter a number between 1 and 10: '))

    if 1 <= user_input <= 10:
        print(f"Thank you! Your number is {user_input}")
        break
    else:
        print('Invalid input. Try again.')
