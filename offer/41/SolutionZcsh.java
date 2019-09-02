import java.util.ArrayList;
import java.util.concurrent.LinkedBlockingQueue;
public class SolutionZcsh {
    public ArrayList<ArrayList<Integer>> FindContinuousSequence(int sum) throws InterruptedException {

        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        LinkedBlockingQueue<Integer> queue = new LinkedBlockingQueue<>();

        int queueSum = 0;

        for (int i = 1; i <= (sum / 2) + 1; i++) {
            queue.put(i);
            queueSum += i;
            while (queueSum > sum) {
                queueSum -= queue.poll();
            }
            if (queueSum == sum && queue.size() != 1) {
                result.add(new ArrayList<>(queue));
            }
        }

        return result;
    }
}
