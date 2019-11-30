
/**
 * Solution class
 *
 * @author 蒋时华
 * @date 2019/11/23
 */
public class Solution {

    int k, rows, cols;
    boolean[][] use;

    public int movingCount(int threshold, int rows, int cols) {
        k = threshold;
        this.rows = rows;
        this.cols = cols;
        use = new boolean[rows][cols];
        int moving = this.moving(k, 0, 0);
        System.out.println(moving);
        return moving;
    }

    public int moving(int k, int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || this.getSum(row, col) > k || use[row][col]) {
            return 0;
        } else {
            use[row][col] = true;
            return 1 + this.moving(k, row, col-1)
                    + this.moving(k, row, col+1)
                    + this.moving(k, row-1, col)
                    + this.moving(k, row+1, col);
        }
    }

    private int getSum(int x, int y) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        while (y > 0) {
            sum += y % 10;
            y /= 10;
        }
        return sum;
    }


}
