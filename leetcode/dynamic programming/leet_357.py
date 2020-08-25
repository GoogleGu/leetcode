class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        counts = [1, 9]
        possible_digit = 9
        for i in range(n-1):
            counts.append(counts[-1] * possible_digit)
            possible_digit -= 1
            if possible_digit < 0:
                break
        return sum(counts[:n+1]) 



