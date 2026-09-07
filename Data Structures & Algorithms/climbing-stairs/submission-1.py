class Solution:
    def climbStairs(self, n: int) -> int:
        
        map = {}

        def climbStair(m: int):
            if m in map:
                return map[m]
            else:
                if m >= 2:
                    map[m] = climbStair(m - 2) + climbStair(m - 1)
                    return map[m]
                else:
                    return 1

        return climbStair(n)