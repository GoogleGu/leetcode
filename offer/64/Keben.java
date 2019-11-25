
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {

    public ArrayList<Integer> maxInWindows(int[] num, int size) {
        if (num == null) {
            return null;
        }
        if (size <= 0 || num.length < size) {
            return new ArrayList<>();
        }

        //大顶堆
        PriorityQueue<Integer> queue = new PriorityQueue<>(num.length, Comparator.reverseOrder());

        for (int i = 0; i < size; i++) {
            queue.add(num[i]);
        }
        ArrayList<Integer> result = new ArrayList<>(size);

        for (int left = 0, right = left+size; right <= num.length; right++, left++) {
            result.add(queue.peek());
            if (right >= num.length) {
                break;
            }
            queue.remove(num[left]);
            queue.add(num[right]);
        }
        return result;
    }

}
