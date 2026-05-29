class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_streak , max_streak = 0,0

        for n in nums:
            if n == 1:
                curr_streak += 1
                max_streak = max(max_streak, curr_streak)
            else:
                curr_streak = 0
        return max_streak