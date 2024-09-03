class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        str_num = ""

        for i in s:
            str_num += str(ord(i) - ord('a') + 1)
        
        for _ in range(k):

            digit_sum = sum(int(value) for value in str_num)

            str_num = str(digit_sum)
        return int(str_num)