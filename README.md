Match-Game
==========

A game to see who can force the other to draw the last match

This a computer version of the desktop game.  In this game, a number of "matches" are laid out on a "desktop."  Each turn, a player can draw up to a certain number (usually 3) of matches.  Whoever draws the last match loses.

Notes:
*To run, download match.py and navigate to its directory in terminal.  Use "python3 match.py" to run
*Utilizes Minimax for AI Logic, so don't expect the computer to be fast for high number of matches or draws
*Default settings for Setup should be:
  -15
  -3
  -h
  -m
  (Note, if m is first, the computer will always win.  Place h first to attempt for perfect play to beat computer)

Noted Bugs:
*In setup, an answer other than "h" or "m" will terminate the program

ToDo:
*Implement Alpha-Beta Pruning to speed up larger games
*Implement web-interface (experiment with Django?) so that users don't have to download and run in terminal