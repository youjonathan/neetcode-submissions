class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # the window len is >= t.len
        # the window must always have all char in t
        # we could try reducing the window until we lose a char?

        if len(t) > len(s):
            return ""

        # brute force: have two pointers that slowly grow smaller
        # check each time if it still contains t