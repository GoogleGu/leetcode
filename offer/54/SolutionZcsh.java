import java.util.concurrent.LinkedBlockingQueue;
public class SolutionZcsh {
    private LinkedBlockingQueue<Character> queue = new LinkedBlockingQueue<Character>();
    private char[] charArray = new char[256];

    public void Insert(char ch) {
        if (++charArray[ch] == 1) queue.add(ch);
    }

    public char FirstAppearingOnce() {
        while (!queue.isEmpty() && charArray[queue.peek()] > 1) queue.poll();
        return queue.isEmpty() ? '#' : queue.peek();
    }
}
