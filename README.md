# Python Mini Projects

A collection of simple, interactive Python mini-projects demonstrating fundamental programming concepts like input/output, loops, conditionals, randomness, and encryption.

## Projects

### 1. Number Guesser (`number_guesser.py`)
A classic number guessing game where you try to guess a randomly generated number within a specified range and guess limit.

**How to play:**
```bash
python3 number_guesser.py
```
- Enter the top range number
- Enter the maximum number of guesses allowed
- Try to guess the randomly generated number
- Get hints if your guess is too high or too low
- Game ends when you guess correctly or run out of guesses

### 2. Password Manager (`password_manager.py`)
A simple CLI password manager that securely stores account credentials using Fernet symmetric encryption from the `cryptography` library.

**Features:**
- Add new passwords with encrypted storage
- View existing passwords (decrypted)
- Key-based encryption using a generated `key.key` file
- Data stored in `passwords.txt`

**Requirements:**
```bash
pip install cryptography
```

**How to use:**
```bash
python3 password_manager.py
```
- Choose `add` to store a new account/password pair
- Choose `view` to see stored credentials
- Type `q` to quit

**Note:** `key.key` and `passwords.txt` are git-ignored for security.

### 3. Quiz Game (`quiz_game.py`)
A simple trivia quiz that tests your knowledge of computer science fundamentals.

**How to play:**
```bash
python3 quiz_game.py
```
- Answer the question about CPU
- Receive immediate feedback on correctness
- Get final score as a percentage

### 4. Rock, Paper, Scissors (`rock_paper_scissors.py`)
Play Rock, Paper, Scissors against the computer.

**How to play:**
```bash
python3 rock_paper_scissors.py
```
- Type `rock`, `paper`, or `scissors`
- Type `q` to quit
- Track wins and losses as you play
- Final score displayed on exit

### 5. Pig Dice Multi-Player Game (`pig_dice_multi_player_game.py`)
A classic multiplayer dice game where players take turns rolling a die to accumulate points, but rolling a 1 loses all points for that turn. First player to reach 50 points wins.

**How to play:**
```bash
python3 pig_dice_multi_player_game.py
```
- Enter number of players (2-4)
- On your turn, choose to **roll** (y) or **hold** (n)
- Rolling: Gain the die value added to your turn score
  - Roll a **1**: Lose all turn points, turn ends immediately
  - Roll 2-6: Points added to turn total; choose to roll again or hold
- Holding: Add turn score to your total, pass to next player
- Game ends when a player reaches 50 points
- Leaderboard shown after each turn
- Winner(s) announced at end (handles ties)

## Requirements

Python 3.x required for all projects.

Only the Password Manager requires an additional dependency:
```bash
pip install cryptography
```

## Getting Started

Clone the repository and run any project directly:
```bash
git clone <repo-url>
cd python_mini_projects
python3 <project_name>.py
```

Each project is self-contained and runs in the terminal. No additional configuration needed.

## License

Educational projects for learning Python fundamentals.
