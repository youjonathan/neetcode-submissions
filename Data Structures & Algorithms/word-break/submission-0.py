class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # my thought process of a brute force method is
        # take s and check against all the words in the wordDict
        # recurse each time you 'find' a match, and then for the newly
        # shortened string, you check again for a match
        # if you reach any end and s is '', then return true
        # otherwise, you return false

        # one immediate optimization we can do is instead of making s.copy
        # we can just index into the string?

        def findMatch(i):
            if i == len(s):
                return True
            for word in wordDict:
                length = len(word)
                if s[i:i+length] == word and findMatch(i+length):
                        return True
            return False
        
        return findMatch(0)