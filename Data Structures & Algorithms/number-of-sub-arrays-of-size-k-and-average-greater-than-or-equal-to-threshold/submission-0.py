class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        curr_sum = 0
        res = 0

        for R in range(len(arr)):
            curr_sum += arr[R]
            if R >= k-1:
                if curr_sum >= target:
                    res +=1
                curr_sum -= arr[R-k+1]
        
        return res


        