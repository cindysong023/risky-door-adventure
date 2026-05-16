import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from risky_door_adventure import (update_game_state, check_game_over, record_data)


def test_update_game_state_adds_score():
    """Test that score increases correctly."""

    outcome = {"message": "safe path", "score_change": 2, "health_change": 0}

    score, health = update_game_state(0, 3, outcome)

    assert score == 2
    assert health == 3


def test_update_game_state_loses_health():


    """Test that health decreases correctly."""

    outcome = {"message": "trap", "score_change": 0, "health_change": -1}

    score, health = update_game_state(5, 3, outcome)

    assert score == 5
    assert health == 2


def test_check_game_over_true():
    """Test game over condition."""

    assert check_game_over(0) is True


def test_check_game_over_false():
    """Test non-game over condition."""

    assert check_game_over(2) is False


def test_record_data():
    """Test that round data is recorded."""

    game_data = []

    outcome = {"message": "treasure", "score_change": 5, "health_change": 0}

    record_data(game_data, 1, "gold", outcome, 5, 3)

    assert len(game_data) == 1
    assert game_data[0]["round"] == 1
    assert game_data[0]["door"] == "gold"
    assert game_data[0]["score"] == 5
    assert game_data[0]["health"] == 3