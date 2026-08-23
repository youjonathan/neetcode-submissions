class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # the window len is >= t.len
        # the window must always have all char in t
        # we could try reducing the window until we lose a char?

        if len(t) > len(s):
            return ""

        # brute force: have two pointers that slowly grow smaller
        # check each time if it still contains t

        tset = {}
        for char in t:
            tset[char] = tset.get(char, 0) + 1
        sset = {}
        for char in s:
            sset[char] = sset.get(char, 0) + 1
        
        for letter in tset:
            tcount = tset[letter]
            scount = sset.get(letter, 0)
            if scount < tcount:
                return ""

        l = 0
        r = len(s) - 1
        
        # i'm a little confused if this is right but
        # my idea is that if i start on the outside, i can slowly move in
        # check if the tset is still all contained in sset
        # if we reach a piece where the count goes below, 
        # then move the other pointer

        while l < r:
            c = s[l]
            sset[c] -= 1
            l += 1
            if c in tset and sset[c] < tset[c]:
                l -= 1
                sset[c] += 1
                break
        
        while r > l:
            c = s[r]
            sset[c] -= 1
            r -= 1
            if c in tset and sset[c] < tset[c]:
                r += 1
                sset[c] += 1
                break

        return s[l : r + 1]