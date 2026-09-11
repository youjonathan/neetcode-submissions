class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        subset = []

        def dfs(i: int):

            if i >= len(nums):
                results.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            dfs(i + 1)

            # don't include
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return results