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

        # after tracing through example 3, we realize we can memoize specific findMatch(i) results so we don't have to recalculate them
        memo = {}
        def findMatch(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for word in wordDict:
                length = len(word)
                if s[i:i+length] == word and findMatch(i+length):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        
        return findMatch(0)