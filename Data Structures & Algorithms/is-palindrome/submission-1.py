import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # attempting space complexity o(1)
        i = 0
        s = re.sub(r'[^a-zA-Z0-9]', '', s).replace(" ", "")
        j = len(s)-1
        res = True
        while i <= len(s)-1 and j >=0:
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else :
                res = False
                break
        return res

        
