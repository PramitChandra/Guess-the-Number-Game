# Guessing Game

# 1. Python will guess one game in a range of 1 to 50 numbers
# 2. Take users input in UserNum
# 3. If UserNum is near +- 10 digits to the actual number give 10 points.
# 4. else if UserNum is near +- 5 digits to the actual number give 25 points.
# 5. else if UserNum is exactly the same give 50 points
# 6. Show the output and score


def playAgain(): # Recursive Function - A function calling itself.
    pg = input("\nDo you want to play again y/n: ")
    if pg == 'y' or pg == 'n':
        return pg
    else:
        return playAgain()


import random

def guessGame():

    playA = 'y'
    score = 0

    while playA == 'y':

        computerNum = random.randint(1, 50)
        UserNum = int(input("\n\nGuess any number between 1 to 50: "))

        diff = computerNum - UserNum

        if computerNum == UserNum:
            print("It's the same number, yippee! You get 50 points")
            score = score + 50
            print("Your updated score is: ", score)

        elif diff >= -5 and diff <= 5:
            print("This number is very close to the real number")
            print("UserNum = ", UserNum)
            print("ComputerNum = ", computerNum)
            score = score + 25
            print("Your updated score is: ", score)

        elif diff >= -10 and diff <= 10:
            print("This number is close to the real number")
            print("UserNum = ", UserNum)
            print("ComputerNum = ", computerNum)
            score = score + 10
            print("Your updated score is: ", score)

        else:
            print("Sorry! Your guess is wrong.")
            print("UserNum = ", UserNum)
            print("ComputerNum = ", computerNum)
            print("Your updated score is: ", score)

        playA = playAgain()
    else:
        print("Your Final Score is: ", score)


guessGame()