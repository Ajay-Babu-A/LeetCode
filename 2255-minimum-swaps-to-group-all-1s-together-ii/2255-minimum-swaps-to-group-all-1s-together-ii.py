class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # If there are no 1's, no swaps are needed
        if total_ones == 0:
            return 0
        
        # Find the maximum number of 1's in any subarray of length total_ones
        max_ones = 0
        current_ones = 0
        
        for i in range(total_ones):
            if nums[i] == 1:
                current_ones += 1
        max_ones = current_ones
        
        # Sliding window
        for i in range(total_ones, n + total_ones):
            if nums[i % n] == 1:
                current_ones += 1
            if nums[(i - total_ones) % n] == 1:
                current_ones -= 1
            max_ones = max(max_ones, current_ones)
        
        # Minimum swaps is the number of 0's in the best window
        return total_ones - max_ones
