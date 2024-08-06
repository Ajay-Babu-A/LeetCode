class Solution:
    def minimumPushes(self, word: str) -> int:
            
        # Count letter occurrences
        char_frequency = Counter(word)
        
        # Create max heap of frequencies
        frequency_heap = [-freq for freq in char_frequency.values()]
        heapq.heapify(frequency_heap)
        
        total_key_presses = 0
        key_position = 0
        
        while frequency_heap:
            current_freq = -heapq.heappop(frequency_heap)
            total_key_presses += (key_position // 8 + 1) * current_freq
            key_position += 1
        
        return total_key_presses