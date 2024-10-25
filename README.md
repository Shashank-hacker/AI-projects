# AI-projects
Uses MinMax to play perfect tictactoe on command line
Key Components of the Code
Game Class:

Attributes:
game: A 3x3 grid initialized with None values representing empty cells.
player: Indicates the current player, starting with "o".
moves: A list of available moves represented as tuples of coordinates.
utility: Keeps track of the game's state (1 for "x" win, -1 for "o" win, 0 for ongoing/draw).
Methods:
move(mov): Makes a move for the current player and updates the game state.
switch(): Switches the current player.
check(): Checks the game state to see if there's a winner or if the game is still ongoing.
show(): Displays the current state of the game board.
Static methods for game logic:
actions(game): Returns available moves.
result(game, action): Returns the resulting game state after a move.
utilitycheck(x): Checks the utility of a game state.
player(game): Determines whose turn it is.
minvalue(game) and maxvalue(game): Implements the minimax algorithm to evaluate game states.
terminal(game): Checks if the game has ended.
Game Modes:

twoplayer(): Allows two human players to play against each other.
noobai(): Allows a human player to play against a basic AI that makes random moves.
proaix(): Allows a human player to play against a perfect AI that uses the minimax algorithm to make optimal moves.
Main Function:

Prompts the user to select a game mode and starts the corresponding function.
Improvements and Suggestions
Input Validation:

The code currently does not handle invalid inputs gracefully. Adding error handling for non-integer inputs or out-of-range coordinates would improve user experience.
Refactoring:

The check() and utilitycheck() methods have similar logic. They could be refactored to reduce redundancy.
The switch() method could be simplified using a dictionary to map player symbols.
User Interface:

The current text-based interface could be enhanced with clearer prompts or a graphical user interface using libraries like Tkinter.
Game Reset:

After a game ends, providing an option to restart or exit would enhance usability.
Documentation:

Adding docstrings to methods and classes would help others understand the code better.
AI Improvement:

The basic AI (noobai) could be enhanced to use a simple heuristic instead of random moves, making it a more challenging opponent.
