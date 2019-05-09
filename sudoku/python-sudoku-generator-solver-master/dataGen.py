#This file generates sudoku puzzles and saves them into a file along with their corresponding solution
import sudoku, time, csv, os

#create one sudoku board and its corresponding solution
def dataGen():
    p = sudoku.perfectSudoku()
    solved=getBoardData(p)
    s = sudoku.puzzleGen(p)
    unsolved=getBoardData(s[0])

    return [solved,unsolved]


#Serialize a sudoku board into an array of 81 numbers
def getBoardData(sudoku):
    '''Serializes a sudoku board'''
    row = []
    for i in range(81):
        if i in range(0,81):
            row.append(sudoku[i].returnSolved())

    return(row)

#write n new sudoku boards to the data files
def writeLines(n):
    puzzle= open("puzzle.csv",'a')
    answer= open("answer.csv",'a')
    for i in range(n):
        data=dataGen()
        puzzle.write(str(data[1])[1:-1]+"\n")
        answer.write(str(data[0])[1:-1]+"\n")
    answer.close()
    puzzle.close()
while(True):
    writeLines(100)
    print("100 completed")
