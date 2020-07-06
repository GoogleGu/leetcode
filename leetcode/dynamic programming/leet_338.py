
class Solution:
    def countBits(self, num: int):

        counts = [0, 1]

        while len(counts) < num+1:
            new_counts = [count + 1 for count in counts]
            counts.extend(new_counts)

        return counts[:num+1]
