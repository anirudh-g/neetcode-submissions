class Solution:
    def isValid(self, s: str) -> bool:
         stack = []
         close_map = {")" : "(", "}":"{" , "]":"["}

         for st in s:
            if st in close_map:
                if not stack:
                    return False
                if stack[-1] != close_map[st]:
                    return False
                stack.pop()
            else:
                stack.append(st)
         return not stack
                
                
        