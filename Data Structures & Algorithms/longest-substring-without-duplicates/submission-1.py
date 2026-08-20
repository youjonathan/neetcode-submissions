class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # my first thought is that this will probably involve a set to check for duplicates
        # i'm guessing you could iterate over the characters, add to a count of nonduplicates, add that character to the set, then reset once you run into a duplicates

        length = 0
        max_length = 0
        letters = set()

        for char in s:
            if char in letters:
                max_length = max(max_length, length)
                length = 0
                letters = set()
            length += 1
            letters.add(char)

        max_length = max(max_length, length)
        return max_length
            