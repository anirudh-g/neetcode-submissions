class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash sets can be used to de-dup an array. in this case , the question is whether there is a duplicate.
        # in this case , it is enough to compare the len of original array and hashed set.
        return False if len(set(nums)) == len(nums) else True