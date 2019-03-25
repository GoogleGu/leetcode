import java.util.List;
import java.util.ArrayList;
public class Solution {
    private static final List<Integer> list = new ArrayList<>();

    private static int CURRENT_MAX_INDEX = 1;

    static {
        list.add(1);
        list.add(2);
    }

    public  int RectCover(int target) {

        if (target <= 0) {
            return 0;
        }
        
        if (list.size() >= target) {
            return list.get(target - 1);
        }

        for (int i = CURRENT_MAX_INDEX + 1; i <= target; i++) {
            list.add(list.get(i - 1) + list.get(i - 2));
        }
        CURRENT_MAX_INDEX = target;
        return list.get(target - 1);

    }

}
