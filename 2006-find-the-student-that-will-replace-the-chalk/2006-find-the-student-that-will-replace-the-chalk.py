class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total_chalk = sum(chalk)
        k %= total_chalk
        
        for i, usage in enumerate(chalk):
            if k < usage:
                return i
            k -= usage