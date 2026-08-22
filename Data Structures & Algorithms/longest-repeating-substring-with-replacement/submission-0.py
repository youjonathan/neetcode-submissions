class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # start left and right pointer on first index
        # move right pointer while adding to set
        # keep a count of the first char
        # keep a count of non-first char
        # when count of non-first char increases above k, move left pointer to the right until it reaches first non-first char and repeat process as if everything from the left of left pointer doesn't exist
        # keep taking max length

        l = 0
        r = 0

        max_length = 0
        length = 0
        non = 0

        while r < len(s):
            if s[r] != s[l]:
                non += 1
                if non > k:
                    l += 1
                    r = l
                    non = 0
                    length = 0
            length += 1
            r += 1                
            max_length = max(max_length, length)

        return max_length
