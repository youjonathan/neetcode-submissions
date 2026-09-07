class Solution:
    def climbStairs(self, n: int) -> int:
        
        one = 1
        two = 2

        for i in range(3, n + 1, 2):
            one = one + two
            two = one + two
        
        return two if n % 2 == 0 else one
