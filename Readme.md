### Mancala AI
This is a project fro Introduction to Artificial Intelligence project 2019
The code was entirely written by Piotr Połcik.

This project contains a rather simple implementation of basic version of Mancala board game with simple UI 
created using tkinter. 

The implemented AI is a MiniMax Algorithm with alpha/beta pruning.

### Prerequisites
- Python 3.6 (did not check if the code is backward compatible with older Python version, but I assume it should be)
- installed numpy module

### Running
- First, make sure you have numpy installed
```
pip3 install numpy
```
- In the default setup MiniMax of depth 2 plays against MiniMax of depth 7. 
- To play against the AI simply comment the suggested lines in the mancala.py (no console arguments were added)
- To run the game simply use
``` 
python manacala.py
```

Enjoy!

### Comments
A basic implementation of Monte Carlo Tree search algorithm is also included in the files, although it was not tested thourughly for correctness, 
as the main algorithm was the MiniMax algorithm.

