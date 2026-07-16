class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        """
        To check if the window size does not exceed the k size constraint,
        do r-l > k and if thats the case , remove the left-most element from the window.
        """
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False