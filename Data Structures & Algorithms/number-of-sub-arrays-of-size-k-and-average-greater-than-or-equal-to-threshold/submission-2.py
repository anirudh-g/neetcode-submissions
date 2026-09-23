class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        window_sum = 0
        check_threshold = k * threshold
        ctr = 0

        for R in range(len(arr)):
            window_sum += arr[R]

            if R - L + 1 == k:
                if window_sum >= check_threshold:
                    ctr += 1
                window_sum -= arr[L]
                L += 1
        return ctr
