# AI and Games!
AI and Games is an exploratory project into how AI can help "solve" games! It is a [20 Percent Project](http://www.20time.org/) built for the Post-AP / Advanced Topics Computer Science class at Kent Denver School in Englewood Colorado. It was developed by Ulysses Atkeson '19 and Grant Fitez '20 in 2019.

Both of us are fairly new to Ml, AI and Neural networks, but we made a lot of good progress and we learned a lot. See our writeup [here](https://docs.google.com/document/d/1drWqtxF1tJrTNptr-YXJvmdJ8LfIuHhhoIrkKW88jt8/edit?usp=sharing) and our log [here](https://docs.google.com/document/d/17e8txT_2huo49XWkmmKNHayIwOWlEGgCRoc6z6UW2yI/edit?usp=sharing)

## Files

### README.md
This file ;)

###-- Rock Paper Scissors--
### cleanData.csv
The cleaned data from [roshambo.me](https://roshambo.me/). uncleanedData.csv was run through cleanData.py to get this file.
### cleanData.py
The file that cleaned the data from [roshambo.me](https://roshambo.me/).  This genrated cleanData.csv. 
### main.h5
The saved neural network model from main.py that is loaded by restore.py
### oneHot.csv
The cleaned and one hoted data that is fed into the neural network. It is made by running  oneHotData.py
### oneHotData.py
Takes the clean data and onehots it
### restore.py
The file to run the saved neural network (main.h5) and interface with the user.
### sess.csv
Where restore.py saves its session data
### train.py
The file that takes in oneHot.csv to train the neural network and outputs the saved network to main.h5
### uncleanedData.csv
The raw data from [roshambo.me](https://roshambo.me/)

###--Sudoku-- (Folder)
This folder also includes python-sudoku-generator-solver-master which is a git repo re modified to genrate sudoku boards. We use the sudoku.py file.
###answer.csv
The answers to the puzzle.csv file. in the same order as the puzzle.csv file. currenty contains ~200,000 answers. this is how the neural network checks its guessed answer.
###puzzle.csv
The puzzles that are fed into the nework
###sudoku.h5
The saved network. This one is a little beefy when loaded.
###sudokuRestore.py
The file to load the stored network (sudoku.h5) and test it against a known good board.
###sudokuTrainer.py
The file that takes in puzzle.csv to train the network and saves it as sudoku.h5.
###testing.csv
A list of a few good baords that sudokuRestore.py uses to test the network
