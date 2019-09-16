import java.util.concurrent.LinkedBlockingQueue;
public class SolutionZcsh {
    public int LastRemaining_Solution(int n, int m) throws InterruptedException {

        if (n == 0 || m == 0) {
            return -1;
        }

        LinkedBlockingQueue<Integer> queue = new LinkedBlockingQueue<>();
        for (int i = 0; i < n; i++) {
            queue.put(i);
        }

        for (int i = 1; queue.size() != 1; i++) {
            Integer poll = queue.poll();
            if (i % m != 0) {
                queue.put(poll);
            }
        }
        return queue.poll();
    }

}
