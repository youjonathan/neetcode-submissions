class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # in a specific window, there has to be the same count of letters in that window as in s1

        s1_len = len(s1)
        s1_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        start_i = 0
        
        for start_i in range(len(s2) - s1_len):
            s2_dict = {}
            for i in range(s1_len):
                char = s2[start_i + i]
                s2_dict[char] = s2_dict.get(char, 0) + 1
            
            # print(str(start_i) + " " + str(s2_dict))

            if s1_dict == s2_dict:
                return True

        return False