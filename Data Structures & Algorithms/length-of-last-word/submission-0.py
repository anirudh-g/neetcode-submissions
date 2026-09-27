class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        
        """
        res = 0

        for i in range(len(s) - 1, -1 , -1):
            if res > 0 and s[i] == " ":
                return res
            if res == 0 and s[i] == " ":
                continue
            res += 1
        return res