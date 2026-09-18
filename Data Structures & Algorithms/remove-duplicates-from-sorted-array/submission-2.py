class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        removing duplicates in place means replacing the duplicate elements in place with non duplicate elements from the right. 
        here , keep L as 0 and 1,R in the loop. if L and R are equal, then inc L by 1 and replace L element with R. return L +1 as that would be the length of the unique elements. 
        '''
        if not nums:
            return 0
        L = 0

        for R in range(1, len(nums)):
            if nums[L] != nums[R]:
                L+=1
                nums[L] = nums[R]
        return L+1
        