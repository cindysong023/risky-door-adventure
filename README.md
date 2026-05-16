# Risky Door adventure

## Project Description

Risky Door adventure is a short adventure-style decision-making game created using Python and Tkinter. The player wakes up in a blank space and must choose between different doors in order to escape. Each round contains three unique doors, and each door may lead to a reward, a penalty, or a dangerous consequence. Some doors are safer and provide smaller rewards, and others are riskier and may either help or hurt the player.

The player begins the game with a limited amount of health, represented by a blood bar at the top of the screen. Throughout the game, the player must balance risk and reward while trying to survive all three rounds and earn the highest score possible. The game records the player’s choices, outcomes, score, and health after each round so the results can later be analyzed for patterns in decision-making.

This project demonstrates decision-making under uncertainty because players must make choices based only on the appearance of the doors without knowing the exact outcome ahead of time.

---

## Technologies and Modules Used

This project uses the following Python modules:

- `tkinter` for the graphical user interface (GUI)
- `PIL (Pillow)` for loading and resizing images
- `random` for random door outcomes
- `os` for handling file paths safely

---

## Main Features

- Intro screen with escape-game storyline
- Three rounds of gameplay
- Nine unique door images
- Safe and risky door choices
- Health / blood bar system
- Score tracking
- Win and game-over conditions
- Data recording for each round

---

## Planned Functions

### `choose_door()`
Represents the player choosing a door by clicking one of the door images.

### `get_outcome(door)`
Takes in the chosen door type and returns the result of the player’s decision, such as rewards or health loss.

### `update_game_state(score, health, outcome)`
Updates the player’s score and health based on the chosen door outcome.

### `check_game_over(health)`
Checks whether the player’s health has reached zero and determines whether the game should end.

### `record_data(game_data, round_num, door, outcome, score, health)`
Stores information from each round so the game data can later be analyzed.

---

## Example Use Cases

- A user can play the game for entertainment while making choices between safe and risky options.
- A student can explore how different decisions affect score and survival.
- The recorded game data can later be used to analyze patterns in decision-making behavior, for example how players judge different doors base on the appearance.

---

## File Structure

risky-door-escape/
├── README.md
├── risky_door_adventure.py
├── test_plan.md
├── images/
└── tests/

## How to run the program 

1. Download or clone this repository.

2. Install the required Python package:

```bash
   pip install pillow pytest

3. Run the game:
python risky_door_adventure.py



## Testing
This project includes unit tests for the main game logic functions.

To run the tests: pytest







