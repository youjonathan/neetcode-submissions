class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(x, y, i):
            if i >= len(word):
                return True
            if x >= len(board[0]) or y >= len(board):
                return False
            if board[y][x] != word[i]:
                return False
            return search(x + 1, y, i + 1) or search(x - 1, y, i + 1) or search(x, y + 1, i + 1) or search(x, y - 1, i + 1)

        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if search(x, y, 0):
                    return True
        
        return False