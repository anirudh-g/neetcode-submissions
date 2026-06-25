class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hashsets - if there are no duplicates , then len(set) will be equal to len
        return (len(set(nums)) < len(nums))