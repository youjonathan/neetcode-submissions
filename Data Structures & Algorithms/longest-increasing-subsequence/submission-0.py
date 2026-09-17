class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # okay my first thought is to loop through every index
        # and use that as the starting point
        # then try to find all numbers ahead of it that are greater
        # and when you find a number that is greater, you recurse on that
        # so on example 1, pretend 9 isn't there, you have 1, then you
        # check longest increasing subsequence of the next number that is greater than 1
        # aka 4, and for 4 you should then recurse on 7, which should give you 0
        # then it'll go to 2 and recurse on 2, which will recurse on 3 and 7
        # so that way it's like yeah similar pattern to a lot of DP problems
        # then later on we'll just store each indexes' longest increasing
        # subsequence so for future recursions you don't have to recalculate

        memo = {}
        def findLIS(i) -> int:
            if i in memo:
                return memo[i]
            longest = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(findLIS(j), longest)
            memo[i] = 1 + longest
            return memo[i]

        longest = 1
        for i in range(len(nums)):
            longest = max(findLIS(i), longest)
        
        return longest

"""
traces
Example 1:
findLIS(0) -> pass all so return 1
findLIS(1) -> 4 works -> findLIS(2) -> 2, 3, 3 pass, 7 works -> findLIS(6) -> return 1 so findLIS(2) = 2 so findLIS(1) j=2 is 2, but the loop continues
    2 works -> findLIS(3) -> 3 works -> findLIS(5) -> 3 pass, 7 works -> findLIS(6) -> return 1 so findLIS(5) = 2 so findLIS(3) = 3 so findLIS(1) j=3 is 3
    this iteration continues but max will be 3 so findLIS(1) = 4

Example 2:
findLIS(0) -> 3 works -> findLIS(1) -> 1, 3, 2, 3 pass so return 1, so findLIS(0) inner loop is 1 but the loop continues
    1 works -> findLIS(2) -> 3 works -> findLIS(3) -> 2, 3, pass so return 1, so findLIS(2) inner loop is 1 but loop continues
        2 works -> findLIS(4) -> 3 works -> findLIS(5) -> return 1 so findLIS(4) = 2 so findLIS(2) inner loop is now 2 and the rest are all less so findLIS(2) = 3 so findLIS(0) = 4
"""