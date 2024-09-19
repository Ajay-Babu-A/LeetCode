class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(maxsize=None)
        def compute_all_ways(sub_exp):
            # If the sub-expression is a digit, convert it to an integer
            # and return it as a list.
            if sub_exp.isdigit():
                return [int(sub_exp)]

            # Initialize an empty list to store possible computation results.
            results = []

            # Iterate through each character in the sub-expression.
            for idx, char in enumerate(sub_exp):
                # Check if the current character is an operator.
                if char in '-+*':
                    # Compute all possible results for the left and right
                    # sub-expressions.
                    left_results = compute_all_ways(sub_exp[:idx])
                    right_results = compute_all_ways(sub_exp[idx + 1:])

                    # Iterate through all combinations of left and
                    # right results, and apply the operator.
                    for left_val in left_results:
                        for right_val in right_results:
                            # Perform the appropriate operation based
                            # on the operator.
                            if char == '-':
                                results.append(left_val - right_val)
                            elif char == '+':
                                results.append(left_val + right_val)
                            else:  # char == '*'
                                results.append(left_val * right_val)
          
            # Return all possible computation results for this sub-expression.
            return results

        # Call the helper function on the entire expression to find all
        # different ways to compute the expression.
        return compute_all_ways(expression)
