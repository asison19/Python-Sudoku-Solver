#sudoku solver in python
#Name: Andrew Sison

#returns true if the number is in the row
def isInRow(sudoku, rowNumber, number):
	for i in range(sudokuDimension):
		if (int(sudoku[rowNumber][i]) == number):
			return True
	return False

#returns true if the number is in the column
def isInColumn(sudoku, columnNumber, number):
	for i in range(sudokuDimension):
		if (int(sudoku[i][columnNumber]) == number):
			return True
	return False

#returns true if the number is in the local 3x3 block
def isInBlock(sudoku, rowNumber, columnNumber, number):
	r = rowNumber - (rowNumber % 3)
	c = columnNumber - (columnNumber % 3)

	for i in range(r, r + 3):
		for j in range(c, c + 3):
			if (int(sudoku[i][j]) == number):
				return True
	return False

#checks rows, columns, and local block
def isValid(sudoku, row, column, number):
	return not isInRow(sudoku, row, number) and not isInColumn(sudoku, column, number) and not isInBlock(sudoku, row, column, number)

#Actual algorithm that solves the sudoku
def isSolved(sudoku, emptyMarker):
	for i in range(sudokuDimension):
		for j in range(sudokuDimension):
			if (sudoku[i][j] == emptyMarker):
				for k in range(1, sudokuDimension + 1):
					if (isValid(sudoku, i , j, k)):
						sudoku[i][j] = k
						if (isSolved(sudoku, emptyMarker) ):
							return True
						else:
							sudoku[i][j] = emptyMarker
				return False
	return True

#reads in sudoku file, and puts it into the 2d sudoku array
def readInSudoku(sudokuFile, sudokuDimension, sudoku):
	for i in range(sudokuDimension):
		row = sudokuFile.readline().split(' ')
		for j in range(sudokuDimension):
			sudoku[i][j] = row[j]

#output the sudoku
def outputSudoku(sudokuDimension):
	for i in range(sudokuDimension):
		for j in range(sudokuDimension):
			print(sudoku[i][j], end="")


sudokuDimension = 9
sudokuFile = open("sudokuTest.txt","r")
emptyMarker = "0"

#create empty sudoku 2d array
sudoku = [[0 for x in range(sudokuDimension)] for y in range(sudokuDimension)]
readInSudoku(sudokuFile, sudokuDimension, sudoku) #give empty sudoku 2d array the proper values

print("Here is the Sudoku to solve: ")
outputSudoku(sudokuDimension) #output originalsudoku

if isSolved(sudoku, emptyMarker): #this algorithm returns true once sudoku is solved
	print("Here is the Solved Sudoku: ")
	outputSudoku(sudokuDimension) #output solved sudoku
#end of program