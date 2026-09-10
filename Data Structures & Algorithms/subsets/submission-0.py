class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset_list = []
        path = []

        def build(index: int):
            nonlocal subset_list
            nonlocal path
            if index >= len(nums):
                subset_list.append(path.copy())
                return
            path.append(nums[index])
            build(index + 1)
            path.pop()
            build(index + 1)
        
        build(0)

        return subset_list