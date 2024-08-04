class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        sub_array = []
        mod = (10**9) + 7

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                sub_array.append(current_sum)
                
        sub_array.sort()

        return sum(sub_array[left - 1 : right]) % mod
        
