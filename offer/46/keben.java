
import java.util.ArrayList;
import java.util.List;
public class Solution {
        public int LastRemaining_Solution(int n, int m) {
        if (n < 1) {
            return -1;
        }

        List<Integer> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            list.add(i);
        }

        int index = 0;
        while (list.size() > 1) {
            index = (index + m - 1) % list.size();
            list.remove(index);
        }
        return list.size() == 1 ? list.get(0) : -1;
    }
}
