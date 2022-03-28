import time

class Sudoku:
    def __init__(self, sudoku: list[list[int]]) -> None:
        self.sudoku = sudoku
        self.emptyCoordintes = self.find_empty_space()

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


    def find_possible_value(self, row: int, col: int) -> list[int]:
        if(self.sudoku[row][col] != 0):
            return None
        possibleList: list[int] = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if(self.sudoku[row][i] == 0):
                continue
            if(self.sudoku[row][i] in possibleList):
                possibleList.remove(self.sudoku[row][i])
        for i in range(9):
            if(self.sudoku[i][col] == 0):
                continue
            if(self.sudoku[row][i] in possibleList):
                possibleList.remove(self.sudoku[col][i])
        offsetRow = row - (row % 3)
        offsetCol = col - (col % 3)
        for i in range(3):
            for j in range(3):
                existVar = self.sudoku[offsetRow + i][offsetCol + j]
                if(existVar in possibleList):
                    possibleList.remove(existVar)
        return possibleList
    
    def find_empty_space(self) -> list[(int,int)]:
        result: list[(int,int)] = []
        for i in range(9):
            for j in range(9):
                if(self.sudoku[i][j] == 0):
                    result.append((i,j))
        return result


    def solve(self, count) -> str:
        if(count == len(self.emptyCoordintes)):
            return "SUCC"
        
        corrdination = self.emptyCoordintes[count]
        row = corrdination[0]
        col = corrdination[1]

        possible_value: list[int] = self.find_possible_value(row, col)
        for value in possible_value:
            self.sudoku[row][col] = value

            if self.solve(count+1) == "SUCC":
                return "SUCC"
            
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
    print(simpleS)
    print(simpleS.solve(0))
    print(simpleS)


if __name__ == '__main__':
    main()