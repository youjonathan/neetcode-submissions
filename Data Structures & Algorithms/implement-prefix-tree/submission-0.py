class PrefixTree:

    def __init__(self):
        self.node = dict()

    def insert(self, word: str) -> None:
        curr = self.node
        for char in word:
            if char not in curr:
                # add the key to the node, create the value as a new dict
                curr[char] = dict()
            # move onto next node and next curr
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.node
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
        
        