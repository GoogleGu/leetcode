public class Solution {
       static int count = 0;
    static boolean[][] flag;

    public static int movingCount(int threshold, int rows, int cols) {
        count = 0;
        flag = new boolean[rows][cols];
        find(0, 0, rows, cols, threshold);

        return count;
    }


    private static boolean find(int i, int j, int rows, int cols, int threshold) {
        if (i < 0 || j < 0 || i >= rows || j >= cols) {
            return false;
        }

        if(flag[i][j]){
            return false;
        }
        flag[i][j] = true;
        if (sum(i, j) > threshold ) {
            return false;
        }
        count++;
        find(i, j - 1, rows, cols, threshold);
        find(i, j + 1, rows, cols, threshold);
        find(i - 1, j, rows, cols, threshold);
        find(i + 1, j, rows, cols, threshold);
        return true;
    }

    private static int sum(int i, int j) {
        System.out.println(i + "--" + j);
        String[] iSplit = String.valueOf(i).split("");
        String[] jSplit = String.valueOf(j).split("");
        int sum = 0;

        for (String s : iSplit) {
            sum += Integer.parseInt(s);
        }

        for (String s : jSplit) {
            sum += Integer.parseInt(s);
        }
        System.out.println(sum);
        return sum;
    }
}
