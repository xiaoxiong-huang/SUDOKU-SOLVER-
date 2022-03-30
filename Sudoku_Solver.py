import time

class Sudoku:

    def __init__(self, sudoku: list[list[int]]) -> None:
        #. sudoku board, list of lists.
        self.sudoku = sudoku
        #. coordintes(row,col) for empty block
        self.emptyCoordintes = self.find_empty_space()

    #. useful method to print out the sudoku
    def __str__(self) -> str:
        sudoku = "|---------|---------|---------|\n"
        for i in range(9):
            sudoku += "|"
            for j in range(9):
                temp = self.sudoku[i][j]
                if(temp == 0):
                     sudoku = sudoku + "   "
                else:
                    sudoku = sudoku + " " + str(temp) + " "
                if(j%3 == 2):
                    sudoku += "|"
                if(j==8):
                    sudoku += "\n"
            
            if(i%3 == 2):
                sudoku += "|---------|---------|---------|\n"
            
        return sudoku

    #. this method will find the possible number that can be put on the empty block
    #. repersent by row and col.
    def find_possible_value(self, row: int, col: int) -> list[int]:
        if(self.sudoku[row][col] != 0):
            return None
        # all possible number for a sudoku
        possibleList: list[int] = [1,2,3,4,5,6,7,8,9]
        # check for every row
        for i in range(9):
            if(self.sudoku[row][i] == 0):
                continue
            # if some block have value not 0 and in possible list, remove it
            if(self.sudoku[row][i] in possibleList):
                possibleList.remove(self.sudoku[row][i])
        # check for every col
        for i in range(9):
            if(self.sudoku[i][col] == 0):
                continue
            # if some block have value not 0 and in possible list, remove it
            if(self.sudoku[i][col] in possibleList):
                possibleList.remove(self.sudoku[i][col])
        # off set the row and col to left top block
        offsetRow = row - (row % 3)
        offsetCol = col - (col % 3)
        # for every block in 3X3 square
        for i in range(3):
            for j in range(3):
                existVar = self.sudoku[offsetRow + i][offsetCol + j]
                # if some block have value in possible list, remove it
                if(existVar in possibleList):
                    possibleList.remove(existVar)
        # remaining value in the list is all possible value can be write to that block.
        return possibleList
    
    # find all empty block in a sudoku, return result is list of (row,col)
    def find_empty_space(self) -> list[(int,int)]:
        result: list[(int,int)] = []
        # go through every row and col
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j] == 0):
                    result.append((i,j))
        return result

    # solve the sudoku recursivily
    def solve(self, count) -> str:
        # if we have filled every empty block in a sudoku,
        # we found the solution, so we stop recursive and return SUCC
        if(count == len(self.emptyCoordintes)):
            return "SUCC"
        
        # get the corrdination for a empty block from the empty block list,
        # see more in __init__ about emptyCoordintes[].
        corrdination = self.emptyCoordintes[count]
        row = corrdination[0]
        col = corrdination[1]

        # find the all possible value we can put in this empty block,
        # used function find_possible_value().
        possible_value: list[int] = self.find_possible_value(row, col)

        # recursivily try all value in possible list.
        for value in possible_value:
            self.sudoku[row][col] = value

            # increase the count by 1, means we are moving on to next empty block.
            if self.solve(count+1) == "SUCC":
                return "SUCC"
            
            # in case blow code will run, that means some block later on do not have any possible
            # value that can be put on that block so return FAIL.
            # we want to reset this block to 0 and try another value.
            self.sudoku[row][col] = 0
        
        return "FAIL"

def main():
    
    simpleSudoku = [[6,0,8,7,0,2,1,0,0],
                    [4,0,0,0,1,0,0,0,2],
                    [0,2,5,4,0,0,0,0,0],
                    [7,0,1,0,8,0,4,0,5],
                    [0,8,0,0,0,0,0,7,0],
                    [5,0,9,0,6,0,3,0,1],
                    [0,0,0,0,0,6,7,5,0],
                    [2,0,0,0,9,0,0,0,8],
                    [0,0,6,8,0,5,2,0,3]]
    simpleS = Sudoku(simpleSudoku)
    print("Sudoku before solve:")
    print(simpleS)
    start = time.time()
    # solve the sudoku in place.
    print("Outcome from solve the sudoku: " + simpleS.solve(0))
    end = time.time()
    print("Sudoku after solve:")
    print(simpleS)
    print("Time used to solve the simple Sudoku: " + str(end-start))

    harderSudoku = [[0,7,0,0,4,2,0,0,0],
                    [0,0,0,0,0,8,6,1,0],
                    [3,9,0,0,0,0,0,0,7],
                    [0,0,0,0,0,4,0,0,9],
                    [0,0,3,0,0,0,7,0,0],
                    [5,0,0,1,0,0,0,0,0],
                    [8,0,0,0,0,0,0,7,6],
                    [0,5,4,8,0,0,0,0,0],
                    [0,0,0,6,1,0,0,5,0]]
    harderS = Sudoku(harderSudoku)
    print("Sudoku before solve:")
    print(harderS)
    start = time.time()
    print("Outcome from solve the sudoku: " + harderS.solve(0))
    end = time.time()
    print("Sudoku after solve:")
    print(harderS)
    print("Time used to solve the simple Sudoku: " + str(end-start))



if __name__ == '__main__':
    main()