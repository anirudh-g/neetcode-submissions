class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for ops in operations:
            if ops == 'C':
                ans.pop()
            elif ops == 'D':
                ans.append(ans[-1] * 2)
            elif ops == '+':
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(ops))

        return sum(ans)
        