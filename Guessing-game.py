import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")

    # Input the number range
    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        if start >= end:
            print("❌ Invalid range. Starting number must be less than ending number.")
            return
    except ValueError:
        print("❌ Please enter valid integers for the range.")
        return

    # Select difficulty
    print("\nChoose Difficulty Level:")
    print("1. Easy (10 chances)")
    print("2. Medium (7 chances)")
    print("3. Hard (3 chances)")

    difficulty_map = {'1': 10, '2': 7, '3': 3}
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice not in difficulty_map:
        print("❌ Invalid choice. Please restart the game and select 1, 2, or 3.")
        return

    attempts = difficulty_map[choice]
    target = random.randint(start, end)

    print(f"\n🎮 Game Started! Guess the number between {start} and {end}.")
    print(f"You have {attempts} attempts.\n")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
                break
            except ValueError:
                print("❗ Invalid input. Please enter an integer.")

        if guess == target:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempt(s).")
            break
        elif guess < target:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        if attempt == attempts:
            print(f"\n😢 You've run out of attempts. The correct number was: {target}")

    print("\n✅ Game Over. Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
