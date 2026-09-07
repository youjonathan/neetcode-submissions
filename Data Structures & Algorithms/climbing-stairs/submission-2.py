class Solution:
    def climbStairs(self, n: int) -> int:
        
        map = {}
        map[1] = 1
        map[2] = 2

        for i in range(3, n + 1):
            map[i] = map[i - 1] + map[i - 2]
        
        return map[n]
