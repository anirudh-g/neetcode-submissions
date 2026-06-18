class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashMap_s , hashMap_t = {} , {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in hashMap_s:
                hashMap_s[i] = 1
            else:
                hashMap_s[i] += 1
        
        for j in t:
            if j not in hashMap_t:
                hashMap_t[j] = 1
            else:
                hashMap_t[j] +=1
        
        if hashMap_s == hashMap_t:
            return True
        return False
        
        
        