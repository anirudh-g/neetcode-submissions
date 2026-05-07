class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak : int = 0
        max_streak : int = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0
        return max_streak

        