class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # HashMap based on-pass solution 

        hashmap = {}

        for index , num in enumerate(nums):
            diff = target - num # instead of adding , we take the difference between our target and num and see if that diff is present in the hashmap

            if diff in hashmap:
                return [hashmap[diff], index]
                # say the target is 7 and the current number being processing is 4 , so the diff is 3. if diff is in hashmap , then we take the index of diff and index of curr number
            
            hashmap[num] = index
            

