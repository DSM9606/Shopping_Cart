# Dan Martin Shopping Cart Project

## Shopping Cart Project README FILE 

## Project Description
https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/README.md

## Setting Up Your Environment
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt 

#Step 1 - Navigate to Shopping Cart on the Desktop

#Step 2 - Create a New Virtual environment

In the command line type "conda create -n shopping env

type "n" + ENTER to run the environment

Activate the virtual environment by typing "conda activate shopping-env" into terminal


## Daniel Martin Rocks Paper Scissors Excercise README FILE Sunday 05.30.21
# Martin.Rocks.Paper.Excercise

##### Instructions: write the appropriate setup instructions, and the exact conda, pip, and python commands needed to run the program from scratch


## Part I: Navigate to the correct folder in Terminal:

* I am using a Mac and the Terminal Application to run this program 

**HINT: Navigate to the Rocks, Paper, Scissors App in the terminal by first typing "pwd enter" into terminal to find your present working directory and then "ls -al" to find all of the folders in your current directory also "cd .." to go to the previous enclosing folder if you went into the wrong folder**

> ## Important! My rocks, paper scissors app is on my desktop and is in a folder called: <i> "Martin.Rocks.Paper.Excercise" </i>

> ## The location of the program on my computer is: <i> /Users/martinhsu/desktop/Martin.Rocks.Paper.Excercise <i/>


When I open terminal to get to the correct folder holding the program I type commands in this order to navigate to the correct folder:

#### Step 1: Type "pwd" + ENTER 
#### Step 2: Type "cd desktop" + ENTER 
#### Step 3: Type "cd " + ENTER
#### Step 4: Type "pwd " + ENTER to make sure you have opened the folder Martin.Rocks.Paper.Excercise on the desktop
#### NOTE: After completing these steps in terminal my present working directory (pwd ENTER) was <i> /Users/martinhsu/desktop/Martin.Rocks.Paper.Excercise </i>

## Part II: Set up a new virtual environment
#### Step 1: Type "conda create -n my-game-env python=3.8" + ENTER in the terminal application
#### Step 2: Type "y" + ENTER two times accept terminal conditions

#### Step 3: Type "conda activate my-game-env" + ENTER 

## Part III: Make sure your packages are installed
#### Step 1: Type "pip install -r requirements.txt" + ENTER into terminal
#### Step 2: Type "pip list" + ENTER into terminal


## Part IV: Set your Player's Name
#### Step 1: Navigate to the Martin.Rocks.Paper.Excercise folder in Mac's finder or wherever the file is on your computer
#### Step 2: Type " ctrl + shift + . " to show hidden files like .env on mac
#### Step 3: Open the .env file and change the player name within the quatations to your desired player name. For example if I wanted to make my name Jasmine the text would read PLAYER_NAME="Jasmine"
#### Step 4: Save and close the document


## Part V: Run the Program and Play the game
#### Step 1: Type "python game.py" + ENTER into terminal
#### Step 2: Follow the instructions in terminal to play the computer in rocks, paper, scissors and remember your inputs are case sensitive! Type in rock, paper or scissors + ENTER in terminal to play the computer in a game!