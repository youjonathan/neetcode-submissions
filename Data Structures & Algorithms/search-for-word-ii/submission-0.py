class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # hm. the brute force way is to loop over every letter
        # then recursively check directions until either word is found or all paths are tried at the word's length
        # i'm guessing the better way is to build a trie out of the board, then look for the words

        root = dict()
        curr = root
        for word in words:
            for char in word:
                if char not in curr:
                    curr[char] = dict()
                curr = curr[char]
            curr['*'] = word
            curr = root
        
        result = set()
        path = set()
        def dfs(node, x, y):
            if x >= len(board) or y >= len(board[0]) or y < 0 or x < 0:
                return
            if (x, y) in path:
                return
            if board[x][y] not in node:
                return

            node = node[board[x][y]]
            path.add((x, y))
            if '*' in node:
                result.add(node['*'])
            
            dfs(node, x + 1, y)
            dfs(node, x - 1, y)
            dfs(node, x, y + 1)
            dfs(node, x, y - 1)

            path.remove((x, y))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(root, x, y)

        return list(result)