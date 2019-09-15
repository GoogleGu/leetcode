public class SolutionZcsh {
    public int Sum_Solution(int n) {
        int result = 0;
        boolean b = (n != 0) &&  (result = n + Sum_Solution(n - 1)) != 0;
        return result;
    }
}
