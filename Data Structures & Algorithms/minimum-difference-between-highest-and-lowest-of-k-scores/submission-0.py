class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        first sort the array to make it in a continuous way of lowest to highest. that way, we can pick up the sliding window.

        then, subtract highest i.e R and lowest i.e L in window k , then store it as minimum. the k is fixed , ao inc by L and R by 1 and repeat
        '''
        nums.sort()
        l, r = 0 , k-1
        result = float("inf")

        while r < len(nums):
            result = min(result, nums[r] - nums[l])
            l+=1
            r+=1
        return result

        