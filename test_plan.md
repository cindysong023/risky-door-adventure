## How to Run the Program
Open the terminal and navigate to the project folder. Then run "python risky_door_adventure.py". The game will start and introduce the player to the escape scenario.

## Overview of Gameplay
In this game, the player is trapped in a series of rooms and must choose doors in order to escape. Each door may lead to a safe outcome, a reward, or a penalty such as losing health. After each choice, the game should display what happened and update the player’s score and health. The game continues until the player escapes or loses all health.

### Test 1: Start of the Game
Steps:
- Run the program

Expected Result:
- The game introduces the escape setting
- The player’s starting health and score are shown
- The player is prompted to choose a door

### Test 2: Choosing a Safe Door
Steps:
- Start the game
- Choose a door that is meant to be the safer option

Expected Result:
- The player gains a small reward or safely moves forward
- The player’s health does not decrease
- The updated score and health are displayed

### Test 3: Choosing a Risky Door With a Good Outcome
Steps:
- Start the game
- Choose a risky door

Expected Result:
- The player may receive a larger reward, such as more points or a useful bonus
- The updated score is shown
- The game continues to the next room

### Test 4: Choosing a Risky Door With a Bad Outcome
Steps:
- Start the game
- Choose a risky door

Expected Result:
- The player may lose health or receive a penalty
- The updated health is displayed
- The game continues if health is above zero

### Test 5: Invalid Input
Steps:
- When asked to choose a door, type an invalid answer such as "abc"

Expected Result:
- The program shows an error message
- The player is asked to choose again
- The game does not crash

### Test 6: Game Over Condition
Steps:
- Continue making risky choices until health reaches zero

Expected Result:
- The game displays a game over message
- The final score is shown
- The program ends

### Test 7: Escape / Win Condition
Steps:
- Continue playing until the player reaches the final room

Expected Result:
- The game displays a success or escape message
- The final score and remaining health are shown
- The program ends

### Test 8: Data Recording
Steps:
- Play several rounds of the game

Expected Result:
- The game records each round’s room number, chosen door, outcome, score, and health
- The recorded data can be used later to analyze player decisions