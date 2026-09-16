class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # unoptimal brute force it
        # loop through every substring from longest to shortest
        # once you reach a substring that is a palindrone you return it
        # because you are going from longest to shortest
        
        longest = ""
        for i in range(len(s)):

            one = i
            two = i

            while s[one] == s[two]:
                palindrome = s[one:two+1]
                one -= 1
                two += 1
                if len(palindrome) > len(longest):
                    longest = palindrome

                if one < 0 or two >= len(s):
                    break
            
            one = i
            two = i+1

            if two >= len(s):
                continue

            while s[one] == s[two]:
                palindrome = s[one:two+1]
                one -= 1
                two += 1
                if len(palindrome) > len(longest):
                    longest = palindrome

                if one < 0 or two >= len(s):
                    break
        
        return longest