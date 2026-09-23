class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1

        while L <=R :
            if s[L]!=s[R]:
                return self.checkPalindrome(s, L+1, R) or self.checkPalindrome(s, L, R-1)
            L+=1
            R-=1
        return True            
    

    def checkPalindrome(self, s, L , R):
        while L < R:
            if s[L] != s[R]:
                return False
            L +=1
            R -=1
        return True        