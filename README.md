# Pentago
Pentago game coded in Python using Numpy with two available game modes, Player versus Player (PVP) mode or Computer bots with two level of difficulty.


## Description
Pentago is a two-player abstract strategy board game invented by Tomas Flodén. Like chess, pentago is a two player game and the goal of the two players is to make the other player lose (or at least tie).

Pentago is played on a 6 by 6 board, divided into four 3 by 3 quadrants. There are two players, black and white, who alternate turns. The goal of each player is to get five stones of their color in a row, either horizontally, vertically, or diagonally. Each turn, a player places a stone in an empty space in some quadrant, then chooses a possibly different quadrant to rotate 90 degrees left or right. If both players get five in a row at the same time, or the last move is played with no five in a row, the game is a tie. If a player makes five a row by placing a stone, there is no need to rotate a quadrant: the player wins immediately.
The 6×6 version of Pentago has been strongly solved with the help of a Cray supercomputer at NERSC. With symmetries removed, there are 3,009,081,623,421,558 possible positions. If both sides play perfectly, the first player to move will always win the game.

## Requirements
Python 3.x

## Installation
<ol>
  <li>Clone this repository or download the pentago.py file.</li>
  <li>Make sure you have Python 3.x installed.</li>
  <li>Run menu() in your IDE to start the game.</li>
</ol>


## How to Play
The game is played on a 6x6 board.
Players take turns placing their piece on an empty spot on the board.
After placing a piece, the player must rotate one of the four quadrants 90 degrees clockwise or counterclockwise.
A player wins by getting five of their pieces in a row horizontally, vertically, or diagonally.
If the board is filled with no player winning, the game is a tie.

## Controls
To place a piece, type the row and column number of the desired location (e.g. 1,3).
To rotate a quadrant, type the quadrant rotation to rotate. (e.g. 1 - 1,1,cw. 2- 1,1,ccw. 3 - 2,1,cw )

## License
The code in this repository is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.
