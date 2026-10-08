class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # if the first element is higher than 0 in a sorted array , then there is no way the triplet would sum to 0. Hence break
                break
            if i > 0 and a == nums[i-1]: # if the 2nd element is same as the first element , then skip it , as it would result in the same set of triplets
                continue
            
            l = i+1 # start l only from i+1 , not 0 everytime
            r = len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r] # fixes a anf finds the corresponding 2 elements that in total sum sup to 0

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                