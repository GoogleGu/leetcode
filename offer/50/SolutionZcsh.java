public class SolutionZcsh {
    public boolean duplicate(int numbers[],int length,int [] duplication) {
        boolean[] cache = new boolean[length];
        for (int i = 0; i < length; i++) {
            if (cache[numbers[i]] && (duplication[0] = numbers[i]) != -1) return true;
            cache[numbers[i]] = true;
        }
        return false;
    }
}
