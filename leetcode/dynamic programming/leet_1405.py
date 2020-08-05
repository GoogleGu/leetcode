class Solution:
    def longestDiverseString(self, a, b, c):
        result = []
        cache = [[a, 'a'], [b, 'b'], [c, 'c']]
        
        repeat = 0
        while True:
            cache.sort(reverse=True)
            print(cache)
            if repeat == 2 and cache[0][1] == result[-1]:
                if cache[1][0] == 0:
                    break
                result.append(cache[1][1])
                cache[1][0] -= 1
                repeat = 0
            else:
                if cache[0][0] == 0:
                    break
                result.append(cache[0][1])
                cache[0][0] -= 1
                if result[-1] == cache[0][1]:
                    repeat += 1
                else:
                    repeat = 0

        return ''.join(result)


if __name__ == "__main__":
    print(Solution().longestDiverseString(3, 3, 3))