import random

def getHighestScore():
    # Read highest score from file
    try:
        file = open('highest_score.txt', 'r')
        highest_score = int(file.read())
        file.close()
        return highest_score
    except IOError:
        file = open('highest_score.txt', 'w')
        file.write("0")
        file.close()
        return 0


def setHighestScore(highestScore):
    # Write highest score from file
    file = open('highest_score.txt', 'w')
    file.write(str(highestScore))
    file.close()
        

def getUserInput():
    userInput = ""
    while not (userInput == "r" or userInput == "p" or userInput == "s" or userInput == "stop") or\
        (userInput == "Rock" or userInput == "Paper" or userInput == "Scissors"):
        userInput = input("==> Choose r/p/s/stop: ")
        if userInput == "r":
            userInput = "Rock"
            break
        elif userInput == 'p':
            userInput = 'Paper'
            break
        elif userInput == 's':
            userInput = 'Scissors'
            break
        elif userInput == 'stop':
            userInput = 'stop'
            break
        else:
            continue
    return userInput


def getCPUInput():
    cpu = random.randint(0,2)
    if cpu == 0:
        return 'Rock'
    elif cpu == 1:
        return 'Paper'
    else:
        return "Scissors"


def gameResult(userInput, cpuInput):
    if userInput == cpuInput:
        print("It's a tie!")
        return 0
    elif (userInput == "Scissors" and cpuInput == "Paper") or\
        (userInput == "Paper" and cpuInput == "Rock") or\
        (userInput == "Rock" and cpuInput == "Scissors"):
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1


def rps():
    
    score = 0
    lives = 5
    print("The current highest score is " + str(getHighestScore()))

    # Start game loop
    while lives >= 0:
        # ask the user rock/paper/scissors
        userChoice = getUserInput()

        if userChoice == 'stop':
            break       # end the game
        
        # get cpu throw
        cpuChoice = getCPUInput()

        #display cpu input
        print("The cpu throws: " + cpuChoice)

        #compare throws and announce the winner
        result = gameResult(userChoice, cpuChoice)

        if result == 1:
            score += 100
        elif result == -1:
            score -= 10
            lives -= 1

        #display the score
        print(f"Your score: {score}")
    
    print(f"Thanks for playing! \nFinal score: {score}")

    #check for a new high score
    highScore = getHighestScore()
    if score > highScore:
        print("A new high score!!")
        setHighestScore(score)

rps()