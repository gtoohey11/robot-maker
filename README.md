# How to run
## Requirements
  - Python3 installed
## Running the command-line application
Download the ZIP for the files in this repository. Add the folder containing these files to your CWD

Run the following command in your terminal terminal
```
python3 menu.py
```

# My implementation
I programmed this project to be a command-line application using python3.

The application prompts the user with two options: create a robot or display the leaderboard and exit Bot-o-mat

A user is allowed to create as many robots as they want. The program collects from the user a name and a type from the list of given types. Next the program randomaly assigns the robot five random tasks and the robot will then execute each task in the amount of time of the task's given duration in milliseconds.

When the user is done creating robots, they can view the stats of their robots before they exit Bot-o-mat. A leaderboard will be displayed holding each robot's name, type, the five tasks it completed, and the total time the robot took to complete its tasks.

The leaderboard will also show how the robot's time scores rank between each other. A list with each robot's time will be displayed and the robot with the lowest time will be declared as the winner.


# BOT-O-MAT

The application collects a name and robot type from the types we list below. For each, it should create a Robot of the type the user chooses, e.g. Larry, Bipedal. 

Given the list of tasks below, the application assigns the Robot a set of five tasks, all of which complete after a duration that shown in milliseconds. 



- Collect a name and robot type from user.
- Instantiate a Robot of the type provided by the user with the name provided by the user
  - for example: Bipedal, Larry
- Set up methods on Robot to complete tasks from the provided list

## Robot
Robot completes tasks and removes them from the list when they are done (i.e. enough time has passed since starting the task).

## Tasks
Tasks have a description and an estimated time to complete.

```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```

## Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```

