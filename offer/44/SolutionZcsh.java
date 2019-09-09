import java.util.Stack;
public class SolutionZcsh {
    public String ReverseSentence(String str) {
        if (str == null || str.trim().length() == 0) {
            return str;
        }
        Stack<String> stack = new Stack<>();
        String[] strings = str.split(" ");
        for (int i = 0; i < strings.length; i++) {
            stack.push(strings[i]);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.empty()) {
            sb.append(stack.pop()).append(" ");
        }
        return sb.toString().substring(0, sb.length() -1);
    }
}
