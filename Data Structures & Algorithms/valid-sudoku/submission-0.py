class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in board:
            digits = set()
            for digit in row:
                if digit == ".":
                    continue
                else:
                    if int(digit) in digits:
                        return False
                    digits.add(int(digit))
        print("passed row test")

        # check cols
        for col in range(len(board)):
            digits = set()
            for row in range(len(board)):
                digit = board[row][col]
                if digit == ".":
                    continue
                else:
                    if int(digit) in digits:
                        return False
                    digits.add(int(digit))
        print("passed col test")

        # check squares
        mylist = [0, 3, 6]
        for i in mylist:
            for j in mylist:
                digits = set()
                for row in range(3):
                    for col in range(3):
                        digit = board[row + i][col + j]
                        if digit == ".":
                            continue
                        else:
                            if int(digit) in digits:
                                return False
                            digits.add(int(digit))
        print("passed square test")

        return True