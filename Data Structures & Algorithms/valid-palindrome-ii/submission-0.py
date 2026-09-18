class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        Allowing for deletion is key here 
        Until that point if both L & R have matched , then both the substrings L+1, R (and) L,R-1 should be checked. 
        as only one delete is allowed , if either is true , return true, else return false 
        '''
        L = 0
        R = len(s)-1

        while L < R:
            if s[L] != s[R]:
                return self.is_palindrome(s, L+1, R) or self.is_palindrome(s, L, R-1)
            L += 1
            R -= 1
        return True

    def is_palindrome(self, s, L, R):
        while L < R:
            if s[L] != s[R]:
                return False
            L+=1
            R-=1
        return True
