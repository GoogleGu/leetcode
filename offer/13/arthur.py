

class Solution:

    def reOrderArray(self, array):

        odds = [num for num in array if num % 2 == 1]
        evens = [num for num in array if num % 2 == 0]
        odds.extend(evens)
        return odds
