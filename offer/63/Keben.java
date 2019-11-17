import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    List<Integer> list = new ArrayList<>();

    public void Insert(Integer num) {
        list.add(num);
        Collections.sort(list);
    }

    public Double GetMedian() {
        if (list.size() % 2 == 0) {
            return (list.get(list.size() / 2) + list.get(list.size() / 2 - 1)) / 2.0;
        }

        return Double.valueOf(list.get(list.size() / 2));
    }


}
