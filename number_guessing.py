import random

###################### Number Guessing Game ###################### 

## The computer will choose a randomly generated number between 1 and 100
## The player will guess a number and be told whether or not the # is too high or low
## There are two difficulties: hard and easy. In easy there are 10 guesses, and hard, 5.


## Choose a random number and ask the player if they want to play on easy or hard
def numberGame():
  number = random.randint(1,100)

  difficulty = input(f"Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard': ")

  if difficulty.lower() == 'easy': 
    chances = 10
  elif difficulty.lower() == 'hard':
    chances = 5
  else : 
    print("I don't recognize that difficulty, I'm going to start you on easy")
    chances = 10

  ## The actual game logic loop- while chances are available let the player guess a number
  ## And tell the player if their guess is too high or too low
  while chances > 0:
    guess = int(input(f"You have {chances} chances left. \nMake a guess: "))

    if guess > number:
      print("My number is lower than that, guess again.")
      chances -= 1
    elif guess < number:
      print("My number is higher than that, guess again.")
      chances -= 1
    else:
      print("You guessed the number, great job!!")
      break

  playAgain = input("Would you like to play again? Hit any button or press 'q' to quit.")

  if playAgain != 'q':
    numberGame()
  else :
    print("Thanks for playing!")

numberGame()


