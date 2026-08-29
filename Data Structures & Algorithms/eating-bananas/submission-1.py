class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary search to find k
        max_k = max(piles)
        
        # if k is the max in piles, the max h is len(piles)
        # if it's less, we find the ceiling of the division per element

        for i in range(max_k): # idk
            l = 0
            r = max_k
            k = r // 2

            min_k = max_k

            curr_h = 0
            for num in piles:
                curr_h += math.ceil(num / k)
            
            if curr_h < h:
                min_k = min(k, min_k)
                r = k
            else:
                l = k

            # this is the binary search
            k = l + (r - l) // 2
        
        return k
