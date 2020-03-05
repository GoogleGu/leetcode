class SolutionZsh {
    public int leastInterval(char[] tasks, int n) {
        if (tasks.length <= 1 || n <=0 ) return tasks.length;

        int[] storage = new int[26];
        int maxCount = 0;
        for (char c: tasks) {
            int index = (c & 0x3f) - 1;
            storage[index]++;
            maxCount = Math.max(storage[index], maxCount);
        }

        int result = (maxCount - 1) * (n + 1);
        for (int i : storage) {
            if (i == maxCount) {
                result++;
            }
        }

        return result < tasks.length ? tasks.length : result;
    }
}