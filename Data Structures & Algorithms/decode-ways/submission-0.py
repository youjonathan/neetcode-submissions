class Solution:
    def numDecodings(self, s: str) -> int:
        
        nums = set()
        for i in range(10, 27):
            nums.add(i)

        # how many ways to decode s[i:]
        def ways(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if int(s[i:i+2]) in nums:
                return ways(i + 1) + ways(i + 2)
            return ways(i + 1)
        
        return ways(0)
