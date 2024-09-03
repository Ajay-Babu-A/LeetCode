class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        # Method 1:
        # str_num = ""

        # for i in s:
        #     str_num += str(ord(i) - ord('a') + 1)
        
        # for _ in range(k):

        #     digit_sum = sum(int(value) for value in str_num)

        #     str_num = str(digit_sum)
        # return int(str_num)

        # Method 2:

        # find the ASCII value

        def convert_num(s):
            return ''.join(str(ord(i) - ord('a') + 1) for i in s)
        
        # sum of digits

        def sum_digits(nums):
            
            return sum(int(d) for d in str(nums))

        num = convert_num(s)

        for _ in range(k):

            num = sum_digits(num)
        
        return num