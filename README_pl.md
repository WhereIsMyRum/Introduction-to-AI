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
<h3 class="why">Powód</h3>
<p class="why">
  Pojekt powstał w ramach przedmiotu Wprowadzenie do Sztucznej Inteligencji (Introduction to Artificial Intelligence), podczas moich studiów magisterskich (Informatyka - Computer Science and Engineering) na Duńskim Uniwersytecie Technicznym (DTU). 
</p>
<h3 class="what">Cel</h3>
<div class="what">
  Celem było zaimplementowanie klienta gry <a target="_blank" href="https://pl.wikipedia.org/wiki/Mankala">Mankala</a> (znanej również jako Kalaha) umożliwiającego grę zarówno z przeciwnikiem jak i ze sztuczną inteligencją (której implementacja była głównym celem projektu).
  Projekt składa się z dwóch głównych części:
  <ul>
    <li> Prosty interfejs graficzny stworzony przy pomocy modułu tkinter </li>
    <li> Implementacja sztucznej inteligencji </li>
  </ul>
</div>
<h3 class="how">Wykonanie</h3>
  <div class="how">Zaimplementowane zostały trzy różne algorytmy, pełniące funkcję przecniwnika AI:
    <ul>
      <li><a target="_blank"  href="https://pl.wikipedia.org/wiki/Algorytm_min-max">Algorytm MiniMax</a></li>
      <li>Algorytm MiniMax z wykorzystaniem <a target="_blank" href="https://pl.wikipedia.org/wiki/Algorytm_alfa-beta">algorytmu Alpha-beta</a>
      <li><a target="_blank" href="https://pl.wikipedia.org/wiki/Monte-Carlo_Tree_Search">Monte Carlo tree search</a></li>
    </ul>
  </div>
<h3 class="technologies">Zastosowane technologie</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
</ul>
<h3 class="usage">Jak korzystać</h3>
<div class="usage">
    <h6>Wymaganie</h6>
    <ul>
      <li>Python 3.6</li>
      <li>Moduł Numpy</li>
    </ul>
    <h6>Play</h6>
    Domyślnie ustawiono starcie pomiędzy dwoma przeciwnikami AI - MiniMax o głębokości 2 oraz 7. Aby zagrać przeciwko AI, zakomentuj linie kodu zasugerowane w pliku mancala.py. Aby uruchomić grę, użyj komendy <i>python manacala.py</i>
</div>
<hr>
<small class="created">Created: March 2019</small>
</body>
</html>
