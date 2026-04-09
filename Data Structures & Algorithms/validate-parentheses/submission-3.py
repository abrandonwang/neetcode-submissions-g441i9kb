class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {']' : '[', '}' : '{', ')' : '('}
        for char in s:
            if char in hashmap:
                if not stack:
                    return False
                elif stack[-1]==hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False