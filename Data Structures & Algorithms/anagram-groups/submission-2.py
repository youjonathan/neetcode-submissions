class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str in hashmap:
                hashmap[sorted_str].append(string)
            else:
                hashmap[sorted_str] = [string]
        
        return(list(hashmap.values()))
