class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0, 0

        """
        Given two strings, initiate two pointers i & j. 
        increment i if an equal is found in j. 
        Otherwise, increment j
        at the end , i should be equal to the length of s if all characters of s is found in t
        """
        while i<len(s) and j <len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)
            
        