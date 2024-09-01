
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        row , col = 0, n
        res = []

        if m*n == len(original):

            for i in range(m):
                res.append(list(original[row : col]))
                row += n
                col += n           

        else:
            return []  

        return res                     
            