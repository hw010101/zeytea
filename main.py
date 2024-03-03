# main.py

from zeytea import ZeyteaGame

def main():
    game = ZeyteaGame()
    print("Zeytea - Sayı Tahmin Etme Oyunu")

    while True:
        guess = int(input("Tahmininizi girin: "))
        result = game.guess_number(guess)
        print(result)

        if result.startswith("Tebrikler"):
            print(f"Toplam deneme sayısı: {game.get_attempts()}")
            break

if __name__ == "__main__":
    main()
