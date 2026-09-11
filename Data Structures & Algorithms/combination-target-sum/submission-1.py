class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        curr = []

        def dfs(i: int, currSum: int):
            if i >= len(nums) or currSum >= target:
                if currSum == target:
                    res.append(curr.copy())
                return
            
            # include this one maybe multiple times
            curr.append(nums[i])
            dfs(i, currSum + nums[i])
            # dfs(i + 1, currSum + nums[i])

            # don't include this one
            curr.pop()
            dfs(i + 1, currSum)

        
        dfs(0, 0)

        # res = [list(t) for t in {tuple(x) for x in res}]
        return res