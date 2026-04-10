class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1

        print(chars)
        for i in t:
            if (i not in chars) or (chars[i] == 0):
                return False
            else:
                chars[i] -= 1
        return True