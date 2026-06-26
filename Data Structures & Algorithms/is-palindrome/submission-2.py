import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower() # keep only alphanum and lowercase everything

        L , R = 0 , len(s) -1

        # initialize two pointers at the beginning and the end . inc & dec respectively until they dont cross each other

        while L < R:
            if s[L] == s[R]:
                L +=1
                R -=1
            else:
                return False
        return True
        