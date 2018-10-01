#
def isInRow(sudoku, rowNumber, number):
	for i in range(sudokuDimension):
		if (sudoku[rowNumber][i] == number):
			return True
	return False

def isInColumn(sudoku, columnNumber, number):
	for i in range(sudokuDimension):
		if (sudoku[i][columnNumber] == number):
			return True
	return False

def isInBlock(sudoku, rowNumber, columnNumber, number):
	r = rowNumber - (rowNumber % 3)
	c = columnNumber - (columnNumber % 3)

	for i in range(r + 3):
		for j in range(c+3):
			if (sudoku[i][j] == number):
				return True
	return False

def isValid(sudoku, row, column, number):
	return ~isInRow(sudoku, row, number) & ~isInColumn(sudoku, column, number) & ~isInBlock(sudoku, row, column, number)

def isSolved(sudoku, emptyMarker):
	for i in range(sudokuDimension):
		for j in range(sudokuDimension):
			if (sudoku[i][j] == 0):
				print("foo")
				for k in range(sudokuDimension + 1):
					if (isValid(sudoku, i , j, k)):
						sudoku[i][j] = k
						if (isSolved(sudoku, emptyMarker) ):
							return True
						else:
							sudoku[i][j] = emptyMarker
				return False	
	return True

def readInSudoku(sudokuFile, sudokuDimension, sudoku):
	location = 0
	for i in range(sudokuDimension):
		for j in range(sudokuDimension):
			sudoku[i][j] = sudokuFile.read(location)
			location += 1

def outputSudoku(sudoku, sudokuDimension):
	for i in range(sudokuDimension):
		for j in range(sudokuDimension):
			print(sudoku[i][j], end="")

sudokuDimension = 9
sudokuFile = open("sudokuTest - Copy.txt","r")
emptyMarker = 0

#instantiate empty sudoku 2d array
sudoku = [[0 for x in range(sudokuDimension)] for y in range(sudokuDimension)]
foo = [[0 for x in range(sudokuDimension)] for y in range(sudokuDimension)]
readInSudoku(sudokuFile, sudokuDimension, sudoku) #create sudoku
print("Here is the Sudoku to solve: ")
outputSudoku(sudoku, sudokuDimension)
if isSolved(sudoku, emptyMarker):
	print("Here is the Solved Sudoku: ")
	outputSudoku(sudoku, sudokuDimension)

