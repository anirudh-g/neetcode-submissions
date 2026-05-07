class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = max_streak = 0
        for i in range(len(nums)):
                current_streak = current_streak + 1 if nums[i] == 1 else 0
                max_streak = max(max_streak, current_streak)

        return max_streak