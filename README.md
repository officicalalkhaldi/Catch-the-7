
<br>

# Catch the Seven

* a grid-based chase game where you control **player2** to catch **player7** before it escapes! The game is played on an 8x8 grid, with **player7** moving randomly and **player2** moving based on your input. The goal is to catch **player7** within 200 turns.



<br>

## Features

- **Dynamic Grid**: The game board updates in real-time using ANSI escape codes.
- **Colorful Display**:
  - **player7** is displayed in **purple**.
  - **player2** is displayed in **Pink**.
  - The grid has a **dark gray background** for better visualization.
- **Interactive Gameplay**: You control **player2** by entering the number of squares and direction to move.
- **Randomized AI**: **player7** moves randomly 1 or 2 squares each turn.


<br>


## How To Play

<br>

### Objective
- catch **player7** by landing on the same square.

<br>

### Controls
- Enter your move in the format `[squares] [direction]`:
  - `squares`: Number of squares to move (1 or 2).
  - `Direction`: Direction to move (`u` for up, `d` for down, `l` for left, `r` for right).
- Example: `2 u` means move **2 squares up**.

<br>

### rules
- you have **20 turns** to catch **player7**.
- If you go out of bounds, the move is invalid, and you must try again.
- **player7** moves randomly after your turn.




<br>

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rabbitq8/catch-the-7.git
   cd catch-the-7
   ```

2. **Run the Game**:
   - Make sure you have python 3 installed.
   - Run the Game:
     ```bash
     python main.py
     ```



<br>

## Code Structure

- **`grid.py`**: Handles grid boundaries and movement validation.
- **`players.py`**: Defines the logic for **player7** (AI) and **player2** (player-controlled).
- **`game.py`**: Manages the game loop, input handling, and board updates.
- **`main.py`**: Entry point to run the game.


<br>

## Screenshots

<br>

* Initial Board

```
          Welcome to Catch the 7

  ------------------------------------------

     1| █ 7 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     2| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     3| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     4| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     5| █ 0 █ 0 █ 0 █ 0 █ 0 █ 2 █ 0 █
     6| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     7| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     8| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █

  ------------------------------------------

  [-] turn : 1
  [-] Player2 position: (5, 6)
  [-] White : 0
  [-] Black : 0

  [-] input : [squares] [direction] (e.g., '2 u' for 2 squares up)
  Directions: 'u' (up), 'd' (down), 'l' (left), 'r' (right)
  Enter your move: 2 u
```

<br>

* After Move
```
          Welcome to Catch the 7

  ------------------------------------------

     1| █ 0 █ 0 █ 7 █ 0 █ 0 █ 0 █ 0 █
     2| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     3| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     4| █ 0 █ 0 █ 0 █ 0 █ 0 █ 2 █ 0 █
     5| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     6| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     7| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █
     8| █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █ 0 █

  ------------------------------------------

  [-] turn : 2
  [-] Player2 position: (4, 6)
  [-] white : 0
  [-] black : 0

  [-] input : [squares] [direction] (e.g., '2 u' for 2 squares up)
  Directions: 'u' (up), 'd' (down), 'l' (left), 'r' (right)
  Enter your move: 1 r
```

<br>

## Dependencies

- python 3.x
- A terminal that supports ANSI escape codes (most modern terminals do).


<br>


## Contributing

Contributions are welcome! If you'd like to improve the game, feel free to:

1. Fork the Repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit Your Changes (`git commit -m 'Add some feature'`).
4. Push to the Branch (`git push origin feature/your-feature`).
5. Open a Pull Request.


<br>

## License

This project is licensed under the MIT License. See the [License](License) file for details.

<br>
<br>
