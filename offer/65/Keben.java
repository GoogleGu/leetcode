public class Solution {
    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
        boolean[] flag = new boolean[matrix.length];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (find(matrix, i, j, rows, cols, flag, str, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean find(char[] matrix, int i, int j, int rows, int cols, boolean[] flag, char[] str, int k) {
        int index = i * cols + j;
        if (i < 0 || j < 0 || i >= rows || j >= cols) {
            return false;
        }

        if (matrix[index] != str[k] || flag[index]) {
            return false;
        }

        if (k == str.length - 1) {
            return true;
        }
        flag[index] = true;
        if (find(matrix, i - 1, j, rows, cols, flag, str, k + 1) ||
                find(matrix, i + 1, j, rows, cols, flag, str, k + 1) ||
                find(matrix, i, j - 1, rows, cols, flag, str, k + 1) ||
                find(matrix, i, j + 1, rows, cols, flag, str, k + 1)) {

            return true;
        }
        
        flag[index] = false;
        return false;
    }
}
