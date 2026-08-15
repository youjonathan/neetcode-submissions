class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""

        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string

        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)

        answer = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            answer.append(s[i:j])
            i = j

        return answer