
import random

# Game configuration
MODE = {
    "easy": {"start": 1, "end": 20, "attempts": 7},
    "medium": {"start": 1, "end": 50, "attempts": 5},
    "hard": {"start": 1, "end": 100, "attempts": 4}
}


def welcome_notes():
    print("\n=======================================")
    print("       Welcome to Number Guessing Game")
    print("=======================================")
    print("\nGame Rules:")
    print("1. Select Easy, Medium or Hard mode.")
    print("2. Guess the randomly selected number.")
    print("3. You have limited attempts to win.")

    for mode, config in MODE.items():
        print(
            f"   {mode.title():<8} --> "
            f"Range: {config['start']}-{config['end']}, "
            f"Attempts: {config['attempts']}"
        )


def get_game_mode():
    mode = input("\nSelect the game mode: ").strip().casefold()

    return MODE.get(mode)


def game_start(start, end, max_attempts):
    target_number = random.randint(start, end)

    print(f"\nGuess a number between {start} and {end}.")

    for attempt in range(1, max_attempts + 1):

        try:
            user_guess = int(input(
                f"Attempt {attempt}/{max_attempts} - Enter your guess: "
            ).strip())

        except ValueError:
            print("Please enter a valid integer!")
            continue

        if user_guess < start or user_guess > end:
            print(f"Please enter a number between {start} and {end}.")
            continue

        if user_guess == target_number:
            print("\nCongratulations! You won!")
            print(f"You guessed correctly in {attempt} attempt(s).")
            return True

        elif user_guess < target_number:
            print("Your guess is too low!")

        else:
            print("Your guess is too high!")

        remaining = max_attempts - attempt
        print(f"Remaining attempts: {remaining}")

    print("\nBetter luck next time!")
    print(f"The correct number was: {target_number}")

    return False


def main():
    welcome_notes()

    game_config = get_game_mode()

    if game_config is None:
        print("\nInvalid game mode selected!")
        print("Please select Easy, Medium or Hard.")
        return

    game_start(
        start=game_config["start"],
        end=game_config["end"],
        max_attempts=game_config["attempts"]
    )

    print("\nGoodbye! Thanks for playing.")


if __name__ == "__main__":
    main()
