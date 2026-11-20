import random

MAX_SCORE = 50

def roll():
    return random.randint(1, 6)

def get_number_of_players():
    while True:
        number_players = input(f"Enter number of players (2 - 4): ")
        if number_players.isdigit():
            number_players = int(number_players)
            if 2 <= number_players <= 4:
                return number_players
        print(f"Invalid input! Please enter a number between 2 and 4.")

def get_player_choice():
    while True:
        choice = input("Roll or hold? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid choice! Please enter 'y' or 'n'.")

def show_scores(player_scores):
    print("\n========== LEADERBOARD ==========")
    for index, score in enumerate(player_scores):
        print(f"Player {index + 1}: {score} points")
    print("=================================\n")

def play_turn(player_idx, player_scores):
    current_score = 0

    print(f"\nPlayer {player_idx + 1}'s turn!")
    print(f"Your total score: {player_scores[player_idx]}")

    while True:
        choice = get_player_choice()

        if choice == "n":
            print(f"Player {player_idx + 1} holds!")
            break

        value = roll()
        print(f"You rolled a {value}!")

        if value == 1:
            print("Oops! You rolled a 1. Your turn score is lost!")
            current_score = 0
            break

        current_score += value
        print(f"Current turn score: {current_score}")
        print(f"Potential total score: {player_scores[player_idx] + current_score}")

    player_scores[player_idx] += current_score

    print(f"\nPlayer {player_idx + 1}'s final score: {player_scores[player_idx]}")

    return player_scores[player_idx] >= MAX_SCORE


def show_winner(player_scores):
    highest_score = max(player_scores)

    winners = [
        index + 1
        for index, score in enumerate(player_scores)
        if score == highest_score
    ]

    print("\n========== GAME OVER ==========")

    if len(winners) == 1:
        print(f"Player {winners[0]} wins with {highest_score} points!")
    else:
        print(f"It's a tie! Players {', '.join(map(str, winners))} win with {highest_score} points!")

    show_scores(player_scores)


def main():
    print("=================================")
    print("       WELCOME TO PIG DICE       ")
    print("=================================")

    players = get_number_of_players()

    player_scores = [0 for _ in range(players)]

    game_over = False

    while not game_over:

        for player_idx in range(players):

            game_over = play_turn(player_idx, player_scores)

            show_scores(player_scores)

            if game_over:
                break

    show_winner(player_scores)


if __name__ == "__main__":
    main()
