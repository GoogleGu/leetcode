from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks).most_common()
        m = counter[0][1]

        # 如果任务足够填满所有m组等待时间
        if len(tasks) >= m * (n+1):
            return len(tasks)

        min_time = (m - 1) * (n + 1)
        k = len([key for key, value in counter if value == m])
        # 如果任务种类超过n+1且能够填满前m-1个等待时间
        if len(counter) > n+1 and len(tasks) > min_time:
            return len(tasks)

        # 否则一定填不满前m-1
        return min_time + k
