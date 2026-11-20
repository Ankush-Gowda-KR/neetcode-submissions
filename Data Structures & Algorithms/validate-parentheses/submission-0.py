class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for x in s:
            if x in pairs:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                pos = pairs[stack.pop()]
                if pos != x:
                    return False
        return len(stack) == 0