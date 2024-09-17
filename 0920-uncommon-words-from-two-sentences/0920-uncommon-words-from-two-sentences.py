class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Step 1 and 2: count word occurrences
        cnt = Counter(s1.split()) + Counter(s2.split())
        # Step 3 and 4: combine counts and filter uncommon words
        return [word for word, count in cnt.items() if count == 1]