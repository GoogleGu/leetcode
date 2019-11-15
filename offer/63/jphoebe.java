import java.util.ArrayList;
import java.util.List;
public class Solution {

    List<Integer> list = new ArrayList<>();

    public void Insert(Integer num) {
        list.add(num);
    }

    public Double GetMedian() {
        if (this.list.size()<=0){
            return null;
        }
        this.quickSort(this.list, 0, list.size() - 1);
        int midd = list.size() / 2;
        if (list.size() % 2 == 0) {
            double result =  (list.get(midd) + list.get(midd-1)) / 2.0;
            return result;
        } else {
            return Double.valueOf(list.get(midd));
        }
    }

    private void quickSort(List<Integer> list, int low, int high) {
        int i, j, temp, t;
        if (low > high) {
            return;
        }
        i = low;
        j = high;
        temp = list.get(low);
        while (i < j) {
            while (temp <= list.get(j) && i < j) {
                j--;
            }
            while (temp >= list.get(i) && i < j) {
                i++;
            }
            if (i < j) {
                t = list.get(j);
                list.set(j, list.get(i));
                list.set(i, t);
            }
        }
        list.set(low, list.get(i));
        list.set(i, temp);
        quickSort(list, low, j - 1);
        quickSort(list, j + 1, high);
    }


}
