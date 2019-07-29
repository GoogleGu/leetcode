import java.util.LinkedHashMap;
public class Solution {
    public int FirstNotRepeatingChar(String str){
        LinkedHashMap <Character, Integer> map = new LinkedHashMap();
        for (int i=0;i<str.length();i++){
            char key = str.charAt(i);
            if (map.containsKey(key)){
                int num= map.get(key);
                map.put(key,num+1);
            }else {
                map.put(key,1);
            }
        }


        for (int j =0;j<str.length();j++){
            char key = str.charAt(j);
            if (map.get(key)==1){
                return j;
            }
        }
        return -1;
    }

}