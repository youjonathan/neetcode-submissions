class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # unoptimal brute force it
        # loop through every substring from longest to shortest
        # once you reach a substring that is a palindrone you return it
        # because you are going from longest to shortest

        start, end = -1, -1
        longest = 0

        def checkPalindromes(s, one, two):
            nonlocal longest, start, end
            while s[one] == s[two]:
                length = two - one + 1
                if length > longest:
                    longest = length
                    start = one
                    end = two

                one -= 1
                two += 1
                if one < 0 or two >= len(s):
                    break

        for i in range(len(s)):

            checkPalindromes(s, i, i)
            
            if i + 1 >= len(s):
                continue

            checkPalindromes(s, i, i + 1)
        
        print(start)
        print(end)
        return s[start : end + 1]