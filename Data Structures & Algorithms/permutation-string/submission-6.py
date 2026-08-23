class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # in a specific window, there has to be the same count of letters in that window as in s1

        s1_len = len(s1)

        if s1_len < len(s2):
            return False

        s1_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        start_i = 0
        
        s2_dict = {}
        for i in range(s1_len):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        for start_i in range(len(s2) - s1_len + 1):
            if s1_dict == s2_dict:
                return True

            end_i = start_i + s1_len - 1
            start_char = s2[start_i]
            end_char = s2[end_i]

            s2_dict[start_char] -= 1
            if s2_dict[start_char] == 0:
                del s2_dict[start_char]

            s2_dict[s2[end_i + 1]] = s2_dict.get(s2[end_i + 1], 0) + 1

        return False