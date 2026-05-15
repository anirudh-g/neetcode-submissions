class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_map = {"(": ")", "{": "}", "[": "]"}

        for ch in s:
            if ch in open_map:
                stack.append(open_map[ch])
            else:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()

        return not stack