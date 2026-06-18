class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = {}

        for i in nums:
            if i not in hash_nums:
                hash_nums[i] = 1
            else:
                return True
        
        return False
        

        