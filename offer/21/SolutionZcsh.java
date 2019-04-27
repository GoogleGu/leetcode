import java.util.Stack;
public class SolutionZcsh {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        Stack<Integer> stack = new Stack<Integer>();
        for (int push = 0,pop = 0; push <= pushA.length; push++) {
            while (pop < popA.length && !stack.isEmpty() && stack.peek() == popA[pop]) {
                stack.pop();
                pop++;
            }
            if (push < pushA.length) {
               stack.push(pushA[push]);
            }
        }
        return stack.isEmpty();
    }
}
