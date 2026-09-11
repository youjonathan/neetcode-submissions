class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def search(x, y, i):
            if i >= len(word):
                return True
            if (x, y) in visited:
                return False
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
                return False
            if board[y][x] != word[i]:
                return False

            visited.add((x, y))
            found = search(x + 1, y, i + 1) or search(x - 1, y, i + 1) or search(x, y + 1, i + 1) or search(x, y - 1, i + 1)
            visited.remove((x, y))
            return found

        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if search(x, y, 0):
                    return True
        
        return False