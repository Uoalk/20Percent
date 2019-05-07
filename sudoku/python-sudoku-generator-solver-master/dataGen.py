import sudoku, time, csv, os

def dataGen():
    p = sudoku.perfectSudoku()
    solved=getBoardData(p)
    s = sudoku.puzzleGen(p)
    unsolved=getBoardData(s[0])

    return [solved,unsolved]



def getBoardData(sudoku):
    '''Serializes a sudoku board'''
    row = []
    for i in range(81):
        if i in range(0,81):
            row.append(sudoku[i].returnSolved())

    return(row)

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
