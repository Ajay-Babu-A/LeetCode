class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        accumulated_xor = list(accumulate(arr, xor, initial=0))

        # Process each query to get the XOR from arr[l] to arr[r].
        # We utilize the property: XOR from arr[l] to arr[r] is
        # accumulated_xor[r + 1] XOR accumulated_xor[l].
        results = [accumulated_xor[r + 1] ^ accumulated_xor[l] for l, r in queries]

        return results