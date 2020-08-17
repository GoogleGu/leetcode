class Solution:
    def maxScore(self, cardPoints, k):
        length = len(cardPoints)
        total = sum(cardPoints)
        if k == length:
            return total

        this_sum = sum(cardPoints[:length-k])
        min_s = this_sum
        for i in range(k):
            print(cardPoints[i+1: i+ length - k+1])
            this_sum = this_sum - cardPoints[i] + cardPoints[i+length-k]
            min_s = min(min_s, this_sum)
        return total - min_s


if __name__ == "__main__":
    print(Solution().maxScore([100,40,17,9,73,75] ,2))