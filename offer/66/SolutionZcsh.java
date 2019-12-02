public class SolutionZcsh {
    public int movingCount(int threshold, int rows, int cols) {

        boolean[][] array = new boolean[rows][cols];


        
        return movingCount(threshold, 0 ,0,array);
    }

    public int movingCount(int threshold, int rowIndex, int colIndex, boolean[][] array) {

        if (rowIndex >= array.length || colIndex >= array[0].length || rowIndex < 0 || colIndex < 0 ||
                array[rowIndex][colIndex] || sum(rowIndex, colIndex) > threshold)return 0;
        
        array[rowIndex][colIndex] = true;

        return movingCount(threshold, rowIndex - 1, colIndex, array)
                + movingCount(threshold, rowIndex + 1, colIndex, array)
                + movingCount(threshold, rowIndex, colIndex - 1, array)
                + movingCount(threshold, rowIndex, colIndex + 1, array)
                + 1;
    }


    private int sum(int x, int y) {
        int sum = 0;
        for (char c : (x + "" + y).toCharArray()) sum += (c & 15);
        return sum;
    }
}
