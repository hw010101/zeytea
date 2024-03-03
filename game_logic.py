# game_logic.py

import random

def generate_number():
    return random.randint(1, 100)

def check_guess(number, guess):
    if guess < number:
        return "Daha yüksek bir sayı tahmin et."
    elif guess > number:
        return "Daha düşük bir sayı tahmin et."
    else:
        return "Tebrikler! Sayıyı doğru tahmin ettin."
