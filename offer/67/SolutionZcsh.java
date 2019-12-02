public class SolutionZcsh {
    public int cutRope(int target) {
        
        if (target == 2) return 1;
        if (target == 3) return 2;
        
        int temp = target % 3;
        if (temp == 0) return (int) Math.pow(3, target / 3);
        if (temp == 1) return (int) Math.pow(3, target / 3 - 1) * 4;
        return (int) Math.pow(3, target / 3) * 2;
    }
}
