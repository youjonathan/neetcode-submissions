class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # okay so this seems similar to the last problem
        # i'm thinking make a hashmap that has num : count
        # decrement the one that leaves the window on the left when it slides
        # then you can easily do max of keys
        # it can't be that simple right?

        count = {}
        maximums = []

        for i in range(k):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for i in range(len(nums) - k + 1):
            maximum = max(count.keys())
            maximums.append(maximum)

            # remove leftmost
            count[nums[i]] -= 1
            if count[nums[i]] == 0:
                del count[nums[i]]
            
            # add rightmost
            if i + k < len(nums):
                num = nums[i + k]
                count[num] = 1 + count.get(num, 0)
        
        return maximums
