class Solution:

    def encode(self, strs: List[str]) -> str:
        # "Hello", "World" -> "5Hello5World"
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output
    def decode(self, s: str) -> List[str]:
        print(s)
        output, i = [], 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j += 1
            number = int(s[i:j])
            output.append(s[j+1:j+1+number])
            i = (j+1+number)
        return output