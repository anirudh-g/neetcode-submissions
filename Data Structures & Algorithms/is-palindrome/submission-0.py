import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s2 = s2.replace(" ", "")
        s2 = s2.lower()
        j = len(s2)-1
        res = True
        while i <= len(s2)-1 and j >=0:
            if s2[i] == s2[j]:
                i+=1
                j-=1
            else :
                res = False
                break
        return res

        
