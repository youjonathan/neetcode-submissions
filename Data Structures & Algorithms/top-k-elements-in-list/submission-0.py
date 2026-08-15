class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 0

        sort_hash = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        answer = list(sort_hash.keys())
        
        return(answer[:k])