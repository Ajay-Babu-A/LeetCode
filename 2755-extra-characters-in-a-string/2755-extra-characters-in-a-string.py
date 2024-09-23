class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        
        n = len(s)
       
        min_extras = [0] * (n + 1)
      
        for i in range(1, n + 1):
            
            min_extras[i] = min_extras[i - 1] + 1
            # Check all possible substrings ending at index 'i'
            for j in range(i):
                # If the substring s[j:i] is in the dictionary
                if s[j:i] in word_set and min_extras[j] < min_extras[i]:
                    min_extras[i] = min_extras[j]
      
        
        return min_extras[n]
