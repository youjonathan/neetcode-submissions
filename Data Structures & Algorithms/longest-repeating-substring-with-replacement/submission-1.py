class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # window length - most freq char <= k
        # okay lowk I'm still stuck on how to get to this statement ^

        l = 0
        r = 0

        max_length = 0
        char_counts = {}

        while r < len(s):
            c = s[r]
            char_counts[c] = char_counts.get(c, 0) + 1
            if ((r - l + 1) - max(char_counts.values()) > k):
                char_counts[s[l]] -= 1
                max_length = max(max_length, sum(char_counts.values()))
                l += 1
            r += 1

        max_length = max(max_length, sum(char_counts.values()))

        return max_length
