class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # the window len is >= t.len
        # the window must always have all char in t
        # we could try reducing the window until we lose a char?

        if len(t) > len(s):
            return ""

        tset = {}
        for char in t:
            tset[char] = tset.get(char, 0) + 1
        
        # the algorithm is check each window edge on the right
        # if you find a window that works, then shrink it from the left
        # once it's shrank to it's min, you save that

        l = 0
        r = 0
        sset = {}
        answer = ""

        for r in range(len(s)):
            sset[s[r]] = sset.get(s[r], 0) + 1
            while all(sset.get(c, 0) >= tset[c] for c in tset):
                if answer == "":
                    answer = s[l:r + 1]
                if r - l + 1 < len(answer):
                    answer = s[l:r + 1]
                sset[s[l]] -= 1
                l += 1

        return answer