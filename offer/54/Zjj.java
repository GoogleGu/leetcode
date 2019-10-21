import java.util.HashMap;
import java.util.ArrayList;
public class Solution {
    HashMap<Character, Integer> map=new HashMap();
    ArrayList<Character> list=new ArrayList<Character>();
    public void Insert(char ch){
        if (map.containsKey(ch)){
            int num =map.get(ch)+1;
            map.put(ch,num);
        }else {
            map.put(ch,1);
        }
        list.add(ch);
    }
    public char FirstAppearingOnce(){
        char returnChar = '#';
        for (char key:list){
            if (map.get(key)==1){
                return key;
            }
        }
        return returnChar;
    }
}