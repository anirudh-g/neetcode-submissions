class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Idea is to have a stack + Map combo. 

        every time an open brace is found , expected closing
        brace is pushed on to the stack in that order. 

        so the the close brace is at the top i.e -1 , then pop it. Else if its not the case or ifthe stack is empty, then say its false
        '''
        stack = []
        brace_map = { "(" : ")", "[" : "]", "{" : "}"}

        for char in s:
            if char in brace_map:
                stack.append(brace_map[char])
            
            else:
                if not stack or stack[-1] != char:
                    return False
                stack.pop()
        
        return not stack