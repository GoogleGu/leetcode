import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
        return execute(matrix , 0 , matrix.length - 1 , 0 , matrix[0].length - 1,
                new ArrayList(matrix.length *  matrix[0].length));
    }

    public ArrayList<Integer> execute(int[][] array, int minX, int maxX
            ,int minY , int maxY , ArrayList<Integer> resultList){

        for (int i = minY; i <= maxY; i++) resultList.add(array[minX][i]);// 上边,左往右
        for (int i = minX + 1; i <= maxX; i++) resultList.add(array[i][maxY]); // 右边,上往下
        for (int i = maxY - 1; i >= minY && maxX != minX; i--) resultList.add(array[maxX][i]);//下边,右往左
        for (int i = maxX - 1; i > minX && minY != maxY; i--) resultList.add(array[i][minY]);// 左边.下往上

        return (array.length *  array[0].length) == resultList.size() ? resultList :
                execute(array, ++minX, --maxX, ++minY, --maxY, resultList);
    }

}
