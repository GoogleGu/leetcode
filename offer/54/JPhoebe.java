import java.util.*;
public class Solution {
    LinkedHashMap<Character, Integer> appearCharSequence = new LinkedHashMap<>();

    public void Insert(char ch) {
        if (!this.appearCharSequence.containsKey(ch)){
            this.appearCharSequence.put(ch, 1);
        }else {
            this.appearCharSequence.remove(ch);
        }
    }

    //return the first appearence once char in current stringstream
    public char FirstAppearingOnce() {
        Iterator<Map.Entry<Character, Integer>> iterator = appearCharSequence.entrySet().iterator();
        if (!iterator.hasNext()){
            return '#';
        }else{
            Map.Entry<Character, Integer> next = iterator.next();
            return next.getKey();
        }
    }
}
