# Chess Engine ♜

A fully functional chess game built using Python and Pygame. This project features an interactive GUI, legal move validation, and a smooth user experience for playing chess. Whether you're a chess enthusiast or a developer looking to explore game development, this project is designed to be both fun and educational.


## Features ✨

- **Interactive GUI**: Play chess with a visually appealing and user-friendly interface.
- **Legal Move Validation**: Ensures all moves adhere to the rules of chess using the `python-chess` library.
- **Piece Highlighting**: Highlights selected pieces and their valid moves for better gameplay clarity.
- **Game State Tracking**: Automatically detects checkmate, stalemate, and other endgame conditions.
- **Custom Graphics**: Uses custom-designed PNG images for chess pieces.
- **Pawn Promotion**: Automatically promotes pawns to queens when they reach the opposite end of the board.
- **Open Source**: Fully open-source and customizable under the MIT License.


## Dependencies 🛠️

- Python 3.x
- Pygame
- Python-Chess

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/DylanBT928/chess-engine.git
   cd chess-engine
   ```
2. Install the required dependencies:
   ```
   pip install chess pygame
   ```
3. Run the game:
   ```
   python chess_engine.py
   ```


## How to Play 🎮

1. **Select a Piece**: Click on the piece you want to move.
2. **Move the Piece**: Click on the destination square.
3. **Pawn Promotion**: If a pawn reaches the opposite end of the board, it will automatically be promoted to a queen.
4. **Game Over**: The game will notify you when it's over (checkmate, stalemate, etc.).


## Code Structure 🗂️

```
chess-engine/
├── resources/               # Contains custom PNG images for chess pieces
├── chess_engine.py          # Main game loop and logic
├── README.md                # Project documentation
└── LICENSE                  # MIT License
```


## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the Project**: Create your own fork of the repository.
2. **Create a Branch**: Make a new branch for your feature or bugfix.
   ```
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**: Commit your changes with a descriptive message.
   ```
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**: Push your changes to your forked repository.
   ```
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**: Submit a pull request to the main repository.

Please ensure your code follows the project's style and includes appropriate documentation.


## License 📜

Licensed under the MIT License. See `LICENSE` for more information.


## Acknowledgments 🙏

- [Python-Chess](https://python-chess.readthedocs.io/en/latest/#) for providing the chess logic and move validation.
- [Pygame](https://www.pygame.org/news) for enabling the creation of the interactive GUI.
