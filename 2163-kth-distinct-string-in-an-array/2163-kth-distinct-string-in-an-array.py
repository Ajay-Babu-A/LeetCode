class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        dic = {}

        for i in arr:

            if i in dic:

                dic[i] += 1
            else:
                dic[i] = 1

        for l, v in dic.items():

            if v == 1:
                k -= 1
                if k == 0:
                    return l
        return "" 