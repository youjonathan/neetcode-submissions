class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_strs = []
        for string in strs:
            sorted_strs.append("".join(sorted(string)))

        indices = {}
        for i, word in enumerate(sorted_strs):
            if word in indices:
                indices[word].append(i)
            else:
                indices[word] = [i]

        answer_indices = []
        for word in indices:
                answer_indices.append(indices[word])

        answer = []
        for n, group in enumerate(answer_indices):
            answer.append([])
            for i in group:
                answer[n].append(strs[i])

        return answer