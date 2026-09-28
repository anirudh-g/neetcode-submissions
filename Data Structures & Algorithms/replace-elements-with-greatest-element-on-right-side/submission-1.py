class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        since its greatest element on the right , reverse iterate in the loop. keep max_val as -1 and do the first replacement. after that keep track of  max val
        """
        max_val = -1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = max_val
            max_val = max(max_val, curr)
        return arr