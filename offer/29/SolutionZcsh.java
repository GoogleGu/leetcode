import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> GetLeastNumbers_Solution(int[] input, int k) {

         ArrayList<Integer> resultList = new ArrayList<Integer>(k);
        if (input.length < k) 
            return resultList;

        heap(input, k);
        for (int i = k; i < input.length; i++) {
            if (input[0] > input[i]) {
                swap(input, 0, i);
                heap(input, k);
            }
        }
        for (int i = 0; i < k; i++) {
            resultList.add(input[i]);
        }
        return resultList;
    }

    public void heap(int[] input, int k) {

        for (int i = k - 1; i > 0; i--) {
            // 计算该父节点的索引,因为左右子节点不用,所以计算方式不同
            int parentIndex = (i & 1) == 1 ? (i - 1) / 2 : (i - 2) / 2;
            if (input[parentIndex] < input[i]) {
                swap(input, parentIndex, i);
            }
        }

    }

    public void swap(int[] input, int i, int j) {

        int temp = input[i];
        input[i] = input[j];
        input[j] = temp;
    }
}
