import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.HashSet;
public class SolutionZcsh {

    public ArrayList<String> Permutation(String str) {

        LinkedList<String> list = new LinkedList<String>();
        if (str == null || str.length() == 0) {
            return new ArrayList<String>();
        }
        exec(str.toCharArray(), 0, list);
        ArrayList<String> result = new ArrayList<String>(list);
        Collections.sort(result);
        return result;
    }

    public void exec(char[] chars, int index, LinkedList<String> list) {

        if ((chars.length - 1) == index) {
            list.add(String.valueOf(chars));
        } else {
            HashSet<Character> hashSet = new HashSet<Character>();
            for (int j = index; j < chars.length; j++) {
                if (!hashSet.contains(chars[j])) {
                    hashSet.add(chars[j]);
                    swap(chars, index, j);
                    exec(chars, index + 1, list);
                    swap(chars, index, j);
                }
            }
        }

    }

    private void swap(char[] chars, int i, int j) {
        if (i != j) {
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
        }
    }
}
