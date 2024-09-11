class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff_bit = start ^ goal

        bit_flips = 0

        while diff_bit:
            # Increment the counter if the least significant bit is 1

            bit_flips += diff_bit & 1
            
            # Right-shift to check the next bit
            
            diff_bit >>= 1
    
        return bit_flips

        