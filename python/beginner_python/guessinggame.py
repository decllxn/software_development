#Make the user gues the secret word until the user gets it righ

secret_word = "giraffe"
guess = "" #initializing an empty variable
guesscount = 0

#using while loop till the user gets it right

while guess != secret_word and guesscount < 3:
    guess = input("Enter guess: ")
    guesscount += 1
    if guesscount == 3:
        print("Out of guesses, YOU LOSE!")

if guess == secret_word:
    print("You win!")

