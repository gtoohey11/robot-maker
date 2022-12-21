import random
import time

# class for a robot object
class Robot:

  # counts number of robots user creates
  robot_count = 0

  # robot tasks mapped to their etas
  tasks = {
            'do the dishes': 1000,
            'sweep the house': 3000,
            'do the laundry': 10000,
            'take out the recycling': 4000,
            'make a sammich': 7000,
            'mow the lawn': 20000,
            'rake the leaves': 18000,
            'give the dog a bath': 14500,
            'bake some cookies': 8000,
            'wash the car': 20000
  }

  # robot types keyed by numbers
  types = {
                1: 'Unipedal',
                2: 'Bipedal',
                3: 'Quadrupedal',
                4: 'Arachnid',
                5: 'Radial',
                6: 'Aeronautical',
                }

  # tasks mapped to phrases that signal the task is completed
  completed_tasks = {
                      'do the dishes': 'dishes are done',
                      'sweep the house': 'house is swept',
                      'do the laundry': 'laundry is done',
                      'take out the recycling': 'recycling is taken out',
                      'make a sammich': 'sammich is made',
                      'mow the lawn': 'lawn is mowed',
                      'rake the leaves': 'leaves are raked',
                      'give the dog a bath': 'dog is bathed',
                      'bake some cookies': 'cookies are baked',
                      'wash the car': 'car is washed'
  }

  # Robot class constructor
  def __init__(self):
    self.robotname = input("Enter a robot name: ")
    self.robotype = ""
    self.task_list = [] # holds the tasks that will be randomly assigned to robot
    self.task_count = 5 # each robot starts with 5 tasks
    self.score = 0 # score will be a time in milliseconds
    Robot.robot_count += 1 # increase number of robots each time Robot object is created

  # allows user to select a type for their robot
  def select_robot_type(self):

    # prints selection of types
    print("Choose a robot type:\n")
    for num, type in Robot.types.items():
        print(num, ' : ', type)

    while True:
        i = input("\nEnter a number 1-6: ")
        # makes sure user chooses a listed robot type
        if int(i)<1 or int(i)>6:
            print("You have entered an invalid number, please try again")
            continue
        else:
            self.robotype = Robot.types[int(i)]
            # once robot has a type, we can assign its tasks
            self.assign_tasks_to_robot()
            break
    return

  # randomly assigns five tasks to a robot
  def assign_tasks_to_robot(self):  
    while self.task_count>0: # check if not all five tasks have been assigned
      task_to_add = random.choice(list(Robot.tasks))
      while True:
        # makes sure robot does not get assigned a task it has already been assigned
        if task_to_add in self.task_list:
          task_to_add = random.choice(list(Robot.tasks))
          continue
        else:
          break
      self.task_list.append(task_to_add)
      self.task_count -= 1

    print("\n{}'s tasks are:\n\n{}".format(self.robotname, '\n'.join(self.task_list)))
    # now robot will do its assigned tasks
    self.execute_tasks()

  # helper function to convert milliseconds into seconds
  # needed for sec parameter of time.sleep(sec) method
  def millis_to_sec(self, millis):
    seconds = (millis/1000)%60
    return seconds

  # makes robot execute its five assigned tasks in the given durations
  def execute_tasks(self):
    print("\nStarting tasks...\n")

    for i in range(len(self.task_list)):
      # update robot's time score
      self.score += Robot.tasks[self.task_list[i]]
      # time the duration of the task's eta
      time.sleep(self.millis_to_sec(Robot.tasks[self.task_list[i]]))
      # print a phrase that indicates the task is complete
      print(self.completed_tasks[self.task_list[i]])

    print("\n{} has completed all five tasks!\n".format(self.robotname))    


# class for a Leaderboard object that holds methods to create Robot objects, store robot results, and
# display a leaderboard when the user is done playing Bot-o-mat
class Leaderboard:

  # constructor for Leaderboard class
  def __init__(self):
    self.robots = [] # list that holds all robots the user has made

  # function that creates Robot objects
  def new_robot(self):
    curr_robot = Robot()
    self.robots.append(curr_robot) # adds robot to list of all user's robots
    curr_robot.select_robot_type() # when user makes a robot, they must select a type for it

  # displays leaderboard when user is done playing
  # displays stats for each robot listing all their completed tasks and the total time each
  # robot took to complete its tasks. Also displays a ranking for lowest time scores to highest time scores
  def display_leaderboard(self):
    scores = {} # this will map robot names to their respective scores
    # checks if user made 0 robots
    if len(self.robots)==0:
      print("You did not create any robots, so there is no leaderboard :(\nThanks for playing Bot-o-mat!")
      exit()

    print('\nLeaderboard of the {} total robots loading...\n\n'.format(Robot.robot_count))
    time.sleep(1)

    for robot in self.robots:
      print('Robot name: {}, Robot type: {}'.format(robot.robotname, robot.robotype))
      print('Tasks completed: {}.'.format(', '.join(robot.task_list)))
      print('Total time taken: {} milliseconds\n'.format(robot.score))
      time.sleep(.5)
      scores[robot.robotname] = robot.score

    print("\nThe final ranking is...\n ")
    time.sleep(1.5)

    # prints ranking with best time on top to lowest time on bottom
    for name, tim in sorted(scores.items(), key=lambda kv: kv[1]):
      print("%s: %s" % (name, tim))

    print("\nThe robot with the lowest time is {}!".format(min(scores, key=scores.get)))
    print("\nThanks for playing Bot-o-mat!")



      


