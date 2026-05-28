class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # maintains the sum at every operation separately, there by avaoiding an additional pass over the array again
        num_stack, res = [], 0
        for ops in operations:
            if ops == '+':
                res += (num_stack[-1] + num_stack[-2])
                num_stack.append(num_stack[-1] + num_stack[-2])
            elif ops == 'C':
                res-= num_stack.pop()
            elif ops == 'D':
                res += ( 2* num_stack[-1])
                num_stack.append(2*num_stack[-1])
            else:
                num_stack.append(int(ops))
                res+= int(ops)
        
        return res

