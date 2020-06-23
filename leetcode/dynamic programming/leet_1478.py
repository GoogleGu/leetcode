class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        if len(houses)<=k:
            return 0
        houses.sort()
        n = len(houses)
        inf = 100*10000+1
        # 3-dim dp:
        # 100 x 100 x 100
        # 在前 i 个房子中，放置了 j 个邮筒， 最后一个邮筒的位置是第 l 个房子
        answer = [[[inf]*n for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for j in range(k):
                for l in range(j,i+1):
                    if j>=i and l==i:
                        answer[i][j][l] = 0
                        continue
                    if j==0:
                        # 只有一个邮筒，它放在了第l个房子的位置
                        answer[i][j][l] = sum([abs(x-houses[l])for x in houses[:i+1]] )
                    elif l<i:
                        # 最后一个邮筒，并不放在最后一个房子的位置
                        answer[i][j][l] = answer[l][j][l] + sum([abs(x-houses[l])for x in houses[l+1:i+1]] )
                    else:
                        # 有多个邮筒，它们放在不同的位置
                        # 开始检索倒数第二个邮筒所有可能的位置
                        tt = inf
                        for ll in reversed(range(j-1,l)):
                            t = answer[ll][j-1][ll] + sum([min(abs(x-houses[ll]),abs(x-houses[l]))for x in houses[ll+1:i+1]] )
                            tt = min(t,tt)
                        answer[i][j][l] = tt
        xx = answer[n-1][k-1]
        return min(xx)
