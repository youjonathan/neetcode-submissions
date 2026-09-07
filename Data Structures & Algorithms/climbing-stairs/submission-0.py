class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climbStair(m: int):
            if m >= 2:
                return climbStair(m - 2) + climbStair(m - 1)
            else:
                return 1

        return climbStair(n)