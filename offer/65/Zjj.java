public class Solution {
    public boolean hasPath(char[] matrix, int rows, int cols, char[] str)
    {
        boolean[] isUsed = new boolean[matrix.length];
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if (handleMatrix(matrix,i,j,rows,cols,isUsed,str,0)){
                    return true;
                }

            }
        }
        return false;
    }

    /**
     *
     * @param matrix 组成矩阵的数组
     * @param i 第几行
     * @param j 第几列
     * @param rows 矩阵总行数
     * @param cols 矩阵总列数
     * @param isUsed 判断的路径是否被使用了 数组
     * @param str 路径字符串
     * @param index 路径字符串的下标
     * @return
     */
    private boolean handleMatrix(char [] matrix,int i,int j,int rows,int cols, boolean[] isUsed,char[] str,int index){
        // 转换成数组的矩阵的第几个下标
        int matrIndex =i*cols+j;
        if (i<0||j<0||i>=rows||j>=cols||matrix[matrIndex]!=str[index]||isUsed[matrIndex]==true){
            return false;
        }
        // 最有一个成功了  就成功了
        if (index==str.length-1){
            return true;
        }
        // 把这个下标  标识为已使用
        isUsed[matrIndex] = true;
        // 前 后 上 下
        if (handleMatrix(matrix,i,j-1,rows,cols,isUsed,str,index+1)||handleMatrix(matrix,i,j+1,rows,cols,isUsed,str,index+1)||handleMatrix(matrix,i-1,j,rows,cols,isUsed,str,index+1)||handleMatrix(matrix,i+1,j,rows,cols,isUsed,str,index+1)){
            return true;
        }
        // 还原这个点为未使用
        isUsed[matrIndex] =false;
        return false;

    }


}