class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Using kadane's algorithm 

        total = sum(nums)
        currSum = maxSum = nums[0]
        currMin = maxMin = nums[0] 

        for n in nums[1:]:
            currSum = max(currSum + n, n)
            maxSum = max(currSum, maxSum)

            currMin = min(currMin + n, n)
            maxMin = min(currMin, maxMin)
        
        if maxSum < 0:
            return maxSum

        return max(maxSum, total - maxMin)