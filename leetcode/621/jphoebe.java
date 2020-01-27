class Solution {
    public int leastInterval(char[] tasks, int n) {
        
        int[] count = new int[26];
        int max = 0;
        for (int i = 0; i < tasks.length; i++) {
            int index = tasks[i] - 'A';
            // 计算每个任务的数量
            count[index]++;
            // 计算最大的任务数量
            if (count[index] > max) {
                max = count[index];
            }
        }
        int taskLen = tasks.length;
        // 最多的人数数量，每个之间需要有n个其他任务间隔，所以需要执行n+1个任务
        int res = (max - 1) * (n + 1);
        // 有相同频率的任务，那么最后也会多出来一个任务（res 本来应该就算上自己本身，但为了减少一次去重处理，直接在这里统一加上）
        for (int i = 0; i < 26; i++) {
            if (count[i] == max) {
                res++;
            }
        }
        // 和原task长度比较是为了，确认最终的时间长度是否长果任务长度，如果n=0的情况下，res<task.length
        return res>taskLen?res:taskLen;
        

    }
}
