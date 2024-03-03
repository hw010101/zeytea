# zeytea.py

from game_logic import generate_number, check_guess

class ZeyteaGame:
    def __init__(self):
        self.number_to_guess = generate_number()
        self.attempts = 0

    def guess_number(self, guess):
        self.attempts += 1
        return check_guess(self.number_to_guess, guess)

    def get_attempts(self):
        return self.attempts

