import java.util.HashSet;

public class SolutionZcsh {

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
        for (int i = 0; i < matrix.length; i++)
            if (matrix[i] == str[0] && hasPath(matrix, cols, str, i, 0, new HashSet<>(str.length))) return true;
        return false;
    }

    /**
     * @param mci matrix的当前坐标值
     * @param sci str 的当前坐标值
     * @return
     */
    boolean hasPath(char[] matrix, int cols, char[] str, int mci, int sci, HashSet<Integer> indexSet) {

        if (indexSet.contains(mci)) return false;
        if (sci + 1 == str.length) return true;
        indexSet.add(mci);

        boolean hasPath = (mci - cols >= 0 && matrix[mci - cols] == str[sci + 1] && hasPath(matrix, cols, str, mci - cols, sci + 1, indexSet)) // 下个字符在上面
                || (mci + cols < matrix.length && matrix[mci + cols] == str[sci + 1] && hasPath(matrix, cols, str, mci + cols, sci + 1, indexSet)) // 下个字符在下面
                || (mci % cols != 0 && matrix[mci - 1] == str[sci + 1] && hasPath(matrix, cols, str, mci - 1, sci + 1, indexSet)) // 下个字符在左边
                || ((mci + 1) % cols != 0 && matrix[mci + 1] == str[sci + 1] && hasPath(matrix, cols, str, mci + 1, sci + 1, indexSet)); // 下个字符在右边

        if (!hasPath) indexSet.remove(mci);
        return hasPath;

    }
}
