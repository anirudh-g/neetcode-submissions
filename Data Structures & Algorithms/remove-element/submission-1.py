class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ctr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ctr] = nums[i]
                ctr+=1
        return ctr
        
        
        



        