class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)

        # Count the words in which all the characters are in the allowed set
        # Summing up the boolean values where True is counted as 1, False as 0
        consistent_words_count = sum(all(char in allowed_chars for char in word) for word in words)

        return consistent_words_count  # Return the total count of consistent words
