//num1,num2分别为长度为1的数组。传出参数
//将num1[0],num2[0]设置为返回结果
import java.util.*;
public class Solution {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        Map map = new HashMap();
        for (int i =0;i<array.length;i++){
            if (map.containsKey(array[i])){
                map.put(array[i],2);
            }else {
                map.put(array[i],1);
            }
        }

        List list = new ArrayList();
        Iterator iterator =map.entrySet().iterator();
        while (iterator.hasNext()){
            Map.Entry entry = (Map.Entry) iterator.next();
            if ((Integer) entry.getValue()==1){
                list.add(entry.getKey());
            }
        }
        num1[0] = (Integer) list.get(0);
        num2[0]=(Integer) list.get(1);
    }
}