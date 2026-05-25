class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder = []
        for log in logs:
            if log =='./':
                continue
            elif log == '../':
                if folder:
                    folder.pop()
            else:
                folder.append(log)
        return len(folder)
        