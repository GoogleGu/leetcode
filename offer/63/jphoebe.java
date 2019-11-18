import java.util.ArrayList;
import java.util.List;
public class Solution {

    List<Integer> list = new ArrayList<>();

    public void Insert(Integer num) {

        if (list.isEmpty()){
            list.add(num);
        }else{
            if (list.get(0) >= num){
                list.add(0, num);
            }else if (list.get(list.size()-1)<=num){
                list.add(num);
            }else{
                for (int i = 0; i < list.size()-1; i++) {
                    Integer current = list.get(i);
                    Integer next = list.get(i+1);
                    if (current <= num && num<=next){
                        list.add(i+1, num);
                        return ;
                    }
                }
            }
        }
    }

    public Double GetMedian() {
        if (this.list.size()<=0){
            return null;
        }
        int midd = list.size() / 2;
        if (list.size() % 2 == 0) {
            double result =  (list.get(midd) + list.get(midd-1)) / 2.0;
            return result;
        } else {
            return Double.valueOf(list.get(midd));
        }
    }


}
