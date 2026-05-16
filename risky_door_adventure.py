"""Risky Door Escape. 
This is a simple three-round escape game where the player chooses between doors.
Each door has a different consequence, such as gaining points or losing health.
"""

import os
import random
import tkinter as tk
from PIL import Image, ImageTk


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
MAX_HEALTH = 3
TOTAL_ROUNDS = 3

DOOR_SIZE = (150, 220)
BLOOD_BAR_SIZE = (180, 40)


def choose_door():
    """Represent the player's door choice.

    In this GUI version, the player chooses by clicking a door image.

    """
    pass


def get_outcome(door_type):
    """Return the outcome for the chosen door type."""

    outcomes = {"safe": {"message": "You found a quiet path forward. +2 points.", "score_change": 2, "health_change": 0, },

        "small_reward": {"message": "You found a small key and gained +3 points.", "score_change": 3, "health_change": 0, },

        "trap": {"message": "A trap was hidden behind the door. -1 health.", "score_change": 0, "health_change": -1, },

        "treasure": {"message": "You found hidden treasure. +5 points.", "score_change": 5, "health_change": 0, },

        "gold": {"message": "The golden room was lucky. +8 points.", "score_change": 8, "health_change": 0, },

        "curse": {"message": "The door was cursed. -1 health.", "score_change": 0, "health_change": -1, },

        "random_risk": random.choice([ { "message": "Risk paid off! You gained +6 points.", "score_change": 6, "health_change": 0, },
            { "message": "Risk failed. You lost -1 health.", "score_change": 0, "health_change": -1, }, ]),}

    return outcomes[door_type]


def update_game_state(score, health, outcome):

    """Update and return the player's score and health."""

    score += outcome["score_change"]
    health += outcome["health_change"]

    if health < 0:
        health = 0

    if health > MAX_HEALTH:
        health = MAX_HEALTH

    return score, health


def check_game_over(health):
    """Return True if health is 0 or lower, or return False."""

    return health <= 0


def record_data(game_data, round_num, door, outcome, score, health):
    """Store data from each round for later analysis."""

    game_data.append({"round": round_num, "door": door, "outcome": outcome["message"], "score": score, "health": health})


def get_image_path(filename):

    """Return the full file path for an image in the images folder."""

    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, "images", filename)


def load_image(filename, size):
    """Load and resize an image from the images folder."""
    image_path = get_image_path(filename)
    image = Image.open(image_path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)


class RiskyDoorEscapeGame:
    """Main GUI game class."""

    def __init__(self):
        """Create the game window and initialize game data."""
        self.root = tk.Tk()
        self.root.title("Risky Door Escape")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
        self.canvas.pack()

        self.score = 0
        self.health = MAX_HEALTH
        self.round_num = 0
        self.game_data = []

        self.door_photos = {}
        self.blood_photos = {}

        self.load_all_images()
        self.show_intro()

    def load_all_images(self):
        """Load all door and blood bar images."""
        for door_num in range(1, 10):
            filename = f"door{door_num}.png"
            key = f"door{door_num}"
            self.door_photos[key] = load_image(filename, DOOR_SIZE)

        for health_num in range(0, MAX_HEALTH + 1):
            filename = f"blood_{health_num}.png"
            self.blood_photos[health_num] = load_image(
                filename,
                BLOOD_BAR_SIZE,
            )

    def clear_screen(self):
        """Clear all items from the canvas."""
        self.canvas.delete("all")

    def show_intro(self):
        """Display the opening screen."""
        self.clear_screen()

        self.canvas.create_text(450, 170, text="You woke up in a blank space.", font=("Arial", 30, "bold"), fill="black")

        self.canvas.create_text(450, 245, text=(
                "There are three rounds of doors.\n"
                "Each door may help you escape, or hurt you.\n"
                "Choose carefully."
            ),

            font=("Arial", 18),
            fill="black",
            justify="center",
        )

        continue_button = tk.Button( self.root, text="Click to Continue", font=("Arial", 16), command=self.start_next_round)

        self.canvas.create_window(450, 365, window=continue_button)

    def update_top_bar(self):
        """Show the blood bar and score at the top of the screen."""
        self.canvas.create_image(130, 40, image=self.blood_photos[self.health])

        self.canvas.create_text(780, 40, text=f"Score: {self.score}", font=("Arial", 18, "bold"), fill="black",)

    def start_next_round(self):
        """Move to the next round or end game."""
        self.round_num += 1

        if self.round_num > TOTAL_ROUNDS:
            self.show_win_screen()
        else:
            self.show_room()

    def get_round_doors(self):
        """Return the three door images and door types for the current round."""
        round_doors = {
            1: [
                ("door1", "safe"),
                ("door2", "trap"),
                ("door3", "gold"),
            ],
            2: [
                ("door4", "treasure"),
                ("door5", "safe"),
                ("door6", "random_risk"),
            ],
            3: [
                ("door7", "curse"),
                ("door8", "small_reward"),
                ("door9", "random_risk"),
            ],
        }

        return round_doors[self.round_num]

    def show_room(self):
        """Show the door choices for the current round."""
        self.clear_screen()
        self.update_top_bar()

        self.canvas.create_text(450, 100, text=f"Round {self.round_num}: Choose a door.", font=("Arial", 24, "bold"), fill="black",)

        doors = self.get_round_doors()
        x_positions = [220, 450, 680]

        for index, door_info in enumerate(doors):
            image_key, door_type = door_info

            door_button = tk.Button(self.root, image=self.door_photos[image_key], command=lambda chosen=door_type: self.handle_door_click(chosen))

            self.canvas.create_window(x_positions[index], 330, window=door_button)

    def handle_door_click(self, door_type):
        """Handle what happens after a player clicks a door."""
        outcome = get_outcome(door_type)

        self.score, self.health = update_game_state(self.score, self.health, outcome)

        record_data(self.game_data, self.round_num, door_type, outcome, self.score, self.health)

        self.show_result(outcome)

    def show_result(self, outcome):
        """Show the result of the player's door choice."""
        self.clear_screen()
        self.update_top_bar()

        self.canvas.create_text(450, 220, text=outcome["message"], font=("Arial", 22, "bold"), fill="black", width=700, justify="center")

        if check_game_over(self.health):
            button_text = "Continue"
            button_command = self.show_game_over
        elif self.round_num == TOTAL_ROUNDS:
            button_text = "Continue"
            button_command = self.show_win_screen
        else:
            button_text = "Next Round"
            button_command = self.start_next_round

        next_button = tk.Button(
            self.root,
            text=button_text,
            font=("Arial", 16),
            command=button_command,
        )

        self.canvas.create_window(450, 360, window=next_button)

    def show_game_over(self):
        """Show the game over screen."""
        self.clear_screen()

        self.canvas.create_text(450, 220, text="Game Over", font=("Arial", 38, "bold"), fill="red")

        self.canvas.create_text(450, 300, text=f"You lost all your health.\nFinal Score: {self.score}", font=("Arial", 20), fill="black", justify="center",
        )

        print("Game Data:")
        for row in self.game_data:
            print(row)

    def show_win_screen(self):
        """Show the escape success screen."""
        self.clear_screen()

        self.canvas.create_text(450, 220, text="You Escaped!", font=("Arial", 38, "bold"), fill="green")

        self.canvas.create_text(450, 300, text=(
                f"Final Score: {self.score}\n"
                f"Health Remaining: {self.health}"
            ),
            font=("Arial", 20),
            fill="black",
            justify="center",
        )

        print("Game Data:")
        for row in self.game_data:
            print(row)

    def run(self):
        """Start the Tkinter event loop."""
        self.root.mainloop()


def main():
    """Create and run the Risky Door Escape game."""
    game = RiskyDoorEscapeGame()
    game.run()


if __name__ == "__main__":
    main()