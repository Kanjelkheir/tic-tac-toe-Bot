# Tic-Tac-Toe AI

This project implements a Tic-Tac-Toe game with an AI opponent that uses the Minimax algorithm to determine the optimal move. The game is built using Python and Pygame for the graphical interface.

## Features

- **Player vs. AI:** Play against an intelligent AI opponent.
- **Minimax Algorithm:** The AI uses the Minimax algorithm to make optimal moves, ensuring a challenging experience.
- **Graphical Interface:** A simple and intuitive graphical interface built with Pygame.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

Additionally, you need to install the Pygame library. You can install it using pip:

```bash
pip install pygame
```

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Kanjelkheir/tic-tac-toe-Bot.git
    cd tic-tac-toe-Bot
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Game

To start the game, run the `runner.py` script:

```bash
python runner.py
```

## How to Play

1.  Upon launching the game, you will be prompted to choose whether to play as 'X' or 'O'.
2.  Click on an empty cell on the board to make your move.
3.  The AI will automatically make its move after yours.
4.  The game ends when a player wins or the board is full (a tie).
5.  You can choose to play again after a game concludes.

## Project Structure

- `tictactoe.py`: Contains the core game logic, including the Minimax algorithm implementation.
- `runner.py`: The main script that handles the Pygame graphical interface and game flow.
- `OpenSans-Regular.ttf`: Font file used in the game.
- `requirements.txt`: Lists the Python dependencies.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.
