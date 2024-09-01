import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        original = np.array(original)
        
        if m*n == len(original):
            return original.reshape(m,n)
        else:
            return []                       
            