class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # for a valid anagram , both strings must have the same characters in the same frequency
        # that is , it requires to build a hasmap for both the string separately and then see if those hashmaps
        # are equal

        hash_s, hash_t = {} , {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        return hash_s == hash_t