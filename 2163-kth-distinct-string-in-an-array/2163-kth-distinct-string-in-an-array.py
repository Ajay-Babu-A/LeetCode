class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for i in count.keys():
            if count[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""