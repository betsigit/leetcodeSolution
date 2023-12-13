class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to keep track of visited numbers
        visit = set()

        # Continue the loop until n is already visited
        while n not in visit:
            # Add the current number to the set of visited numbers
            visit.add(n)
            
            # Calculate the sum of squares of digits
            n = self.sumOfSquares(n)
            
            # If the sum of squares is 1, then the number is happy
            if n == 1:
                return True

        # If the loop ends and n is not 1, then it's not a happy number
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        # Calculate the sum of squares of each digit in the number
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10

        return output
