class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force method is to loop throguh all subarrays and find the one with greatest sum
        # however, you don't need to do this
        # you know that because the subarray has to be contiguous, you can essentially cut out certain subarrays or certain parts of the array since if you sum 2 and -3 it's going to be negative, so there's no use in putting that in the subarray?
        # wait but i'm confused because you could have -2 3 but then after or before that you have like huge numbers and that's the actual subarray?

        running_sum = None
        max_sum = -math.inf

        for num in nums:
            if running_sum == None:
                running_sum = num
            else:
                running_sum += num
            max_sum = max(max_sum, running_sum)
            if running_sum < 0:
                running_sum = None

        return int(max_sum)