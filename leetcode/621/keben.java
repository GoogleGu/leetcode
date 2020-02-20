class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (tasks.length <= 1 || n < 1){
            return tasks.length;
        }
        
        int[] counts = new int[26];
        for (int i = 0; i < tasks.length; i++) {
            counts[tasks[i] - 'A']++;
        }
        Arrays.sort(counts);
        int maxCount = counts[25];
        // 时间 = (最大数 -1) * (n+1) +1
        int retCount = (maxCount - 1) * (n + 1) + 1;
       
       //
        for(int i = 24;i>0;i--){
            if(counts[i]!=maxCount){
                break;
            }
            retCount++;
        }
        return Math.max(retCount, tasks.length);
    }
}
