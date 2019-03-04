public class SolutionZcsh {
    public boolean find(int target, int [][] array) {
        int y = array.length - 1;
        int x = 0;
        int maxX = array[0].length - 1;
        while (y >= 0 && x <= maxX) {
            int current = array[y][x];
            if (target < current) {
                y--;
            } else if (target > current) {
                x++;
            } else {
                return true;
            }
        }
        return false;
    }
}
