# Risky Door Adventure

Risky Door Adventure is a simple adventure game where the player moves through rooms by choosing between different doors. Each door has a different level of risk and reward, so the player must make careful choices to earn points while protecting their health. Some doors give small, safe rewards, while others may give a big reward or a penalty. 

planned functions:
1. choose_door() -- Asks the player which door they want to enter and returns their choice.

2. get_outcome(door) -- Takes in the chosen door and determines what happens, such as a reward, a penalty, or no change.

3. update_game_state(score, health, outcome) -- Updates the player’s score and health based on the result of the chosen door.

4. check_game_over(health) -- Checks whether the player’s health has reached zero and whether the game should end.

5. record_data(round_num, door, outcome, score, health) -- This will store information from each round so the game data can be analyzed later.

# Example use cases: 
-- A user can play the game for fun by making choices between safe and risky options. Additionally, the saved game data of how different choices affect score and survival can later be used to look at patterns in decision making.

## Input Structure
This program does not require an external data file. The user will enter choices directly in the terminal by typing a door option, such as "1", "2", or "3". 

## Game Features
- Multiple rooms with different door choices  
- Safe and risky options with different outcomes  
- Health system that determines survival  
- Game over and escape conditions  
- Data recording for each round





