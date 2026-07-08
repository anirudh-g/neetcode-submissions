class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = best_max = nums[0]

        for n in nums[1:]:
            curr_max = max(n , n+curr_max)
            best_max = max(best_max, curr_max)
        return best_max
        