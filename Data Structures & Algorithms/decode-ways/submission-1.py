class Solution:
    def numDecodings(self, s: str) -> int:
        
        nums = set()
        for i in range(10, 27):
            nums.add(i)

        memo = {}

        # how many ways to decode s[i:]
        def ways(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            if int(s[i:i+2]) in nums:
                memo[i] = ways(i + 1) + ways(i + 2)
            else:
                memo[i] = ways(i + 1)
            return memo[i]
        
        return ways(0)
