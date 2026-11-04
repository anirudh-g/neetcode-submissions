class Solution:
    def calPoints(self, operations: List[str]) -> int:
        num_stack , res = [], 0

        for ops in operations:
            if ops == '+':
                num_sum = num_stack[-1] + num_stack[-2]
                num_stack.append(num_sum)
                res += num_sum
            
            elif ops == 'D':
                num_d = num_stack[-1] * 2
                num_stack.append(num_d)
                res += num_d

            elif ops == 'C':
                removed = num_stack.pop()
                res -= removed  
            else:
                num_stack.append(int(ops))
                res += int(ops)
        
        return res