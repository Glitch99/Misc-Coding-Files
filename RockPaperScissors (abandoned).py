# RockPaperScissors
# Scott Jarvis 2016

def Menu():
    loop = 1
    print("Welcome to the Rock Paper Scissors Python Game Thing!")
    print("Prepare to face off against an awful AI, in the ultimate game of...")
    print("ROCK!")
    print("PAPER!")
    print("SCISSORS!")
    games = 1
    while games > 0:
        games = int(input("How many games of 'Rock Paper Scissors' do you want to play?      "))
        if games <= 0:
            print("Please enter a value greater than 0.")

    return games

def PlayerInput():
    choicemade = 0
    while choicemade == 0:
        choice = input("Rock, Paper, or Scissors?")
        if choice == "Rock" or choice == "rock":
            playermove = 1
            choicemade = 1
        elif choice == "Paper" or choice == "paper":
            playermove = 2
            choicemade = 1
        elif choice == "Scissors" or choice == "scissors":
            playermove = 3
            choicemade = 1
        elif choice == "Shotgun":
            print("Well played. You grab your trusty shotgun, and you blow your computer monitor clean in half.")
            choicemade = 1
            playermove = 4
        else:
            print("Hey, I said Rock, Paper, or Scissors. Stop trying to cheat the system.")
    return playermove
    

def AI():
    RChoice = ()
    randum = random.randint(0,2)
    if randum == 0:
        RChoice = 1
    elif randum == 1:
        RChoice = 2
    elif randum == 2:
        RChoice = 3
        
    return RChoice

    
def Game(playermove, games, RChoice):
    if playermove == 1:
        if RChoice == 1:
            print("You both simultaneously pull rocks out of thin air.")
            print("Recognising that this is now a tie, you both awkwardly shove them back, ready for next time.")
            print("TIE")
        elif RChoice == 2:
            print("You take your rock out, and slowly walk towards the robot.")
            print("Suddenly, it sticks out a tiny scrap of paper.")
            print("You begin to laugh, but the robot somehow stretches the paper out and completely covers you in paper.")
            print("You die a slow and painful death by suffocation.")
            print("LOSS")
        elif RChoice == 2:
            print("The robot in front of you brings out some rather intimidating scissors.")
            print("The blades appear to be roughly the size of your legs.")
            print("Panicking, you throw the tiny pebble in your pocket at the robot's head.")
            print("It somehow flies into the circuit board that composes the brain, and the robot is defeated!")
            print("WIN")        
    elif playermove == 2: 
        if RChoice == 1:
            print("Rock vs Paper.")
            print("Truly, a fight for the ages.")
            print("Though the robot and his rock put up a fight, you easily cover them in paper.")
            print("You feel proud, despite everything.")
            print("WIN")
        elif RChoice == 2:
            print("You both take out your bits of paper, and begin to do the only obvious actions.")
            print("That is, drawing stuff on em.")
            print("After you spend hours on your masterpiece (A doodle of yourself holding a trophy) you finish and slam it onto the ground.")
            print("Right onto the robot's picture, which is an exact duplicate.")
            print("TIE")
        elif RChoice == 3:
            print("Scissors!")
            print("Despite the fact that they're really small (and rather blunt),")
            print("Abandon Ship!" )
            print("")
            print("LOSS"   )
    elif playermove == 3: 
        if RChoice == 1:
            print("")
            print("")
            print("")
            print("")
            print("LOSS")
        elif RChoice == 2:
            print("")
            print("")
            print("")
            print("")
            print("WIN")
        elif RChoice == 3:
            print("")
            print("")
            print("" )
            print("")
            print("TIE")      
    games = games - 1
    return winner, ties, games



games      = Menu()
playermove = PlayerInput()
robotmove  = AI()
winner, ties, games = Game()