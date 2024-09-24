class Solution:
    def longestCommonPrefix(self, nums1: List[int], nums2: List[int]) -> int:
        prefixes = set()

        for num in nums1:
            
            while num:
                
                prefixes.add(num)
            
                num //= 10

        
        max_prefix_length = 0

        
        for num in nums2:
            
            while num:
   
                if num in prefixes:
                    # Update 'max_prefix_length' if this prefix is longer than the current max
                    max_prefix_length = max(max_prefix_length, len(str(num)))
                    # Break the loop as we've found the longest prefix for this number
                    break
                # Update 'num' by removing the last digit
                num //= 10
      

        return max_prefix_length