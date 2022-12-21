from robot import Leaderboard

# class for a Menu object which operates the menu the user interacts with at comand line
class Menu:

    # constructor for menu object
    def __init__(self):
        self.leaderboard = Leaderboard() # create a leaderboard for the game

    # display's the menu of user options on the command line
    def display_menu(self):
        print("What would you like to do?\n")
        print("1 : Create a robot")
        print("2 : Print leaderboard and exit Bot-o-mat\n")

    # runs the Bot-o-mat program. Introduces user to the game and displays the menu when the user
    # wants to keep creating robots
    def run(self):
        print("Welcome to Bot-o-mat!\n\nIn this simulator, you can create a robot that will complete a\n"\
            "set of five random tasks. Each task takes an established amount of time to complete.\n"\
                "You can create as many robots as you like, and when you're finished making robots,\n"\
                    "you can compare the times of all your robots by printing the leaderboard!\n")
        while True:
            self.display_menu()
            option = input("Enter option 1 or 2: \n")

            # option for when user wants to make a robot
            if int(option)==1:
                self.leaderboard.new_robot()
                continue
                
            # option for when user wants to see their robots' results and exit the game
            if int(option)==2:
                self.leaderboard.display_leaderboard()
                break
            
            # makes sure user chooses one of the two given options
            else:
                print("You have entered an invalid option, please try again")
                continue

if __name__=="__main__":
    Menu().run() # runs the program


            

