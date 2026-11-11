class WordDictionary:

    def __init__(self):
        self.node = dict()

    def addWord(self, word: str) -> None:
        curr = self.node
        for char in word:
            if char not in curr:
                curr[char] = dict()
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool:

        def searchHelper(node, i):
            if i == len(word):
                return '*' in node

            if word[i] == '.':
                for key in node:
                    if searchHelper(node[key], i + 1):
                        return True
                return False

            if word[i] not in node:
                return False
            return searchHelper(node[word[i]], i + 1)
        
        return searchHelper(self.node, 0)


