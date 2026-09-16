class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        There are 2 indices at play, L & R. 
        If R - L >k then return False
        Use a window set. add number to it. if number is already there then return True. Else False
        '''
        window = set()
        L =0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L]) # slide the window by removing the left most element ( as the elemnt's duplicate is not found ) and inc by 1.
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
