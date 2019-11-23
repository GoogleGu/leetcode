import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Solution class
 *
 * @author 蒋时华
 * @date 2019/11/23
 */
public class Solution {

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {

        List<List<Integer>> startList = new ArrayList<>();
        // [] >> [][]
        char[][] maze = new char[rows][cols];
        int tempRow = 0, tempCol = 0;
        for (int i = 0; i < matrix.length; i++) {
            if (tempCol == cols) {
                tempRow++;
                tempCol = 0;
            }
            maze[tempRow][tempCol] = matrix[i];
            if (str[0] == matrix[i]) {
                startList.add(Arrays.asList(tempRow, tempCol));
            }
            tempCol++;
        }
        boolean[][] use = new boolean[rows][cols];
        for (List<Integer> startNode : startList) {
            use[startNode.get(0)][startNode.get(1)] = true;
            boolean b = this.get(startNode, maze, str, 1, use);
            if (!b){
                use[startNode.get(0)][startNode.get(1)] = false;
            } else{
                return true;
            }
        }
        return false;
    }

    private boolean get(List<Integer> startNode, char[][] maze, char[] str, int index, boolean[][] use) {
        if (index >= str.length){
            return true;
        }
        int maxX = maze.length-1;
        int maxY = maze[0].length-1;
        Integer x = startNode.get(0);
        Integer y = startNode.get(1);
        boolean left = false, right = false, up = false, down = false;
        // 左
        if (y > 0 && str[index] == maze[x][y-1] && !use[x][y - 1]) {
            use[x][y-1] = true;
            left = this.get(Arrays.asList(x, y-1), maze, str, index+1, use);
            if (!left){
                use[x][y-1] = false;
            }
        }
        // 右
        if (y < maxY && str[index] == maze[x][y+1] && !use[x][y + 1]) {
            use[x][y+1] = true;
            right = this.get(Arrays.asList(x, y+1), maze, str, index+1, use);
            if (!right){
                use[x][y+1] = false;
            }
        }
        // 上
        if (x > 0 && str[index] == maze[x - 1][y] && !use[x - 1][y]) {
            use[x - 1][y] = true;
            up = this.get(Arrays.asList(x - 1, y), maze, str, index+1, use);
            if (!up){
                use[x - 1][y] = false;
            }
        }
        // 下
        if (x < maxX && str[index] == maze[x + 1][y] && !use[x + 1][y]) {
            use[x + 1][y] = true;
            down = this.get(Arrays.asList(x + 1, y), maze, str, index+1, use);
            if (!down){
                use[x + 1][y] = false;
            }
        }
        return left || right || up || down;
    }

}
