# AI and Games!
AI and Games is an exploratory project into how AI can help "solve" games! It is a [20 Percent Project](http://www.20time.org/) built for the Post-AP / Advanced Topics Computer Science class at Kent Denver School in Englewood Colorado. It was developed by Ulysses Atkeson '19 and Grant Fitez '20 in 2019.

Both of us are fairly new to Ml, AI and Neural networks, but we made a lot of good progress and we learned a lot. See our writeup [here](https://docs.google.com/document/d/1drWqtxF1tJrTNptr-YXJvmdJ8LfIuHhhoIrkKW88jt8/edit?usp=sharing) and our log [here](https://docs.google.com/document/d/17e8txT_2huo49XWkmmKNHayIwOWlEGgCRoc6z6UW2yI/edit?usp=sharing)

## Files

### README.md
This file ;)

### -- Rock Paper Scissors -- (In main dir)
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

### -- Sudoku -- (Folder)
This folder also includes python-sudoku-generator-solver-master which is a git repo we modified to generate sudoku boards. We use the sudoku.py file.
### answer.csv
The answers to the puzzle.csv file. in the same order as the puzzle.csv file. currently contains ~200,000 answers. this is how the neural network checks its guessed answer.
### puzzle.csv
The puzzles that are fed into the network
### sudoku.h5
The saved network. This one is a little beefy when loaded.
### sudokuRestore.py
The file to load the stored network (sudoku.h5) and test it against a known good board.
### sudokuTrainer.py
The file that takes in puzzle.csv to train the network and saves it as sudoku.h5.
### testing.csv
A list of a few good boards that sudokuRestore.py uses to test the network

## Installation

### Pre Requirements
* Access to a computer and the internet
* Some knowledge of computers and computer science (helpful but not required)

### Install
#### Python
TensorFlow requires python 3.6 however, the most recent version is 3.7. Follow [this](https://realpython.com/installing-python/) and pick the most recent version fo 3.6
#### Tensorflow
Follow [this](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html) to install TF. I know this says 3.7 but it will break if you have 3.7 so keep 3.6

### Running the program
#### RPS
If you just want to play the computer run restore.py (command will depend on how you installed python. it will be either `python restore.py` or just `restore.py`)
![1](/img/1.png)

If you want to recreate it from scratch, first run `python cleanData.py` then `python oneHotData.py` then `python train.py` and then see above. You might not need `python` in front depending on your install. Also `python train.py` will probably take a while so dont be too worried about it.
![2](/img/2.png)

#### Sudoku
If you just want to see what we have done run sudokuRestore.py (command will depend on how you installed python. it will be either `python sudokuRestore.py` or just `sudokuRestore.py`) the top is the neural networks guess and the bottom is the real answer.
![3](/img/3.png)

If you want to recreate it from scratch, first run `python sudokuTrainer.py`or just `sudokuTrainer.py` and then see above. This programs auto saves every 10 minutes so don't be afraid to quit the program and come back to it. you can also run udokuRestore.py while this is running to see if improvements are happening!
![4](/img/4.png)
