public class Solution {
    public int movingCount(int threshold, int rows, int cols)
    {
        boolean[][] sign = new boolean[rows][cols];
        return count(threshold,rows,cols,sign,0,0);
    }

    public int count(int threshold, int rows, int cols,boolean[][] sign,int i,int j){
        if (i<0||j<0||i>=rows||j>=cols||sign[i][j]||sum(i)+sum(j)>threshold){
            return 0;
        }
        sign[i][j] = true;
        // 上下左右
        return count(threshold,rows,cols,sign,i-1,j)+count(threshold,rows,cols,sign,i+1,j)+count(threshold,rows,cols,sign,i,j-1)+count(threshold,rows,cols,sign,i,j+1)+1;
    }

    public int sum(int index){
        int count = 0;
        while (index!=0){
            count = count+ index%10;
            index = index/10;
        }
        return count;
    }
}