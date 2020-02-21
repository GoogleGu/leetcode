EDIT_COST = {
    'delete': 1,
    'insert': 1,
    'substitute': 1,
}


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        source, target = word1, word2
        n, m = len(source), len(target)
        distances = [[0 for _ in range(m+1)] for _ in range(n+1)]

        distances[0][0] = 0
        for i in range(1, n+1):
            distances[i][0] = distances[i-1][0] + EDIT_COST['delete']
        for j in range(1, m+1):
            distances[0][j] = distances[0][j-1] + EDIT_COST['insert']

        for i in range(1, n+1):
            for j in range(1, m+1):
                del_cost = distances[i-1][j] + EDIT_COST['delete']
                ins_cost = distances[i][j-1] + EDIT_COST['insert']
                if source[i-1] != target[j-1]:
                    sub_cost = distances[i-1][j-1] + EDIT_COST['substitute']
                else:
                    sub_cost = distances[i-1][j-1]
                distances[i][j] = min(del_cost, ins_cost, sub_cost)
        return distances[n][m]