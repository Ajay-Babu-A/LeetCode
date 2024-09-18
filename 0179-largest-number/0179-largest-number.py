class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        nums_str = [str(num) for num in nums]

        nums_str.sort(key=cmp_to_key(self.compare_numbers))

        if nums_str[0] == "0":
            return '0'

        return "".join(nums_str)

    def compare_numbers(self, a: str, b: str):
            if a + b < b + a:
                return 1
            else:
                return -1