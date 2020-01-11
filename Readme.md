<!--### Mancala AI
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
as the main algorithm was the MiniMax algorithm.-->

<html>
<body>
<h1 class="title">Mancala AI</h1>
<h3 class="why">Why</h3>
<p class="why">
  This project was created during Introduction to Artificail Intelligence course, during my MSc of Computer Science and Engineering stuides.
</p>
<h3 class="what">What</h3>
<div class="what">
  This is an implementation of the <a target="_blank" href="https://en.wikipedia.org/wiki/Mancala">Mancala</a> (also known as Kalaha) game, that allows the player to play against an AI, or against another player.
  The implementation consists of two main parts:
  <ul>
    <li> Simple GUI implemented using tkinter </li>
    <li> The AI implementation </li>
  </ul>
</div>
<h3 class="how">How</h3>
  <div class="how">Three different algorithms can be found in this implementation:
    <ul>
      <li><a target="_blank"  href="https://en.wikipedia.org/wiki/Minimax">MiniMax</a></li>
      <li>MiniMax with <a target="_blank" href="https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning">Alpha-beta pruning</a>
      <li><a target="_blank" href="https://pl.wikipedia.org/wiki/Monte-Carlo_Tree_Search">Monte Carlo tree search</a></li>
    </ul>
  </div>
<h3 class="technologies">Technologies used</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
</ul>
<h3 class="usage">How to use</h3>
<div class="usage">
  <span>
  <span>
    <h6>Prerequisites</h6>
    <ul>
      <li>Python 3.6</li>
      <li>Numpy module</li>
    </ul>
  </span>
  <span>
    <h6>Play</h6>
     In the default setup MiniMax of depth 2 plays against MiniMax of depth 7. To play against the AI simply comment the sugges ted lines in the mancala.py (no console arguments were added). To run the game simply use <i>python manacala.py</i>
  </span>
  </span>
</div>
<hr>
<small class="created">Created: March 2019</small>
</body>
</html>
