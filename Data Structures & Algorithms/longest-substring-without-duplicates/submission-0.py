class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        L = 0 
        length = 0

        for R in range(len(s)):
            while s[R] in char:
                char.remove(s[L])
                L +=1
            char.add(s[R])

            length = max(length , R-L+1)
        
        return length