class Trie:
    def __init__(self):
        # Initialize each Trie node with 26 pointers for each lowercase letter in the alphabet
        self.children = [None] * 26
        # Initialize a variable to keep count of the number of words passing through this node
        self.count = 0

    def insert(self, word):
        # Start from the root node
        node = self
        for char in word:
            # Convert character to the corresponding index (0-25 for 'a'-'z')
            index = ord(char) - ord('a')
            # If the child node for this character doesn't exist, create it
            if node.children[index] is None:
                node.children[index] = Trie()
            # Move to the child node
            node = node.children[index]
            # Increment the count for each node that is part of a word
            node.count += 1

    def search(self, word):
        # Start from the root node
        node = self
        # To gather the cumulative count of all prefixes of the searched word
        total_count = 0
        for char in word:
            # Convert character to index
            index = ord(char) - ord('a')
            # If the node doesn't have a child at this index, return current total count
            if node.children[index] is None:
                return total_count
            # Move to the child node
            node = node.children[index]
            # Add the node's count to the total count
            total_count += node.count
        # Return the total count which represents the sum of the prefix scores for the word
        return total_count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Create an instance of the Trie
        trie = Trie()
        # Insert each word into the trie, building up prefix counts
        for word in words:
            trie.insert(word)
        # Retrieve and return the sum of the prefix scores for each word
        return [trie.search(word) for word in words]