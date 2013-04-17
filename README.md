Match-Game
==========

A game to see who can force the other to draw the last match

This a computer version of the desktop game.  In this game, a number of "matches" are laid out on a "desktop."  Each turn, a player can draw up to a certain number (usually 3) of matches.  Whoever draws the last match loses.

Notes:</ br>
*To run, download match.py and navigate to its directory in terminal.  Use "python3 match.py" to run</ br>
*Utilizes Minimax for AI Logic, so don't expect the computer to be fast for high number of matches or draws</ br>
*Default settings for Setup should be:</ br>
  -15</ br>
  -3</ br>
  -h</ br>
  -m</ br>
  (Note, if m is first, the computer will always win.  Place h first to attempt for perfect play to beat computer)</ br>

Noted Bugs:</ br>
*In setup, an answer other than "h" or "m" will terminate the program</ br>

ToDo:</ br>
*Implement Alpha-Beta Pruning to speed up larger games</ br>
*Implement web-interface (experiment with Django?) so that users don't have to download and run in terminal</ br>