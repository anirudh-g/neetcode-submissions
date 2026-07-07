class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        total = 0
        for n in nums:
            total += n
            self.prefix_sum.append(total)


    def sumRange(self, left: int, right: int) -> int:

        if left <=right:
            preleft = self.prefix_sum[left-1] if left > 0 else 0
            return (self.prefix_sum[right] - preleft)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)