import java.util.PriorityQueue;

public class SolutionZcsh {

    private PriorityQueue<Integer> min = new PriorityQueue<>();

    private PriorityQueue<Integer> max = new PriorityQueue<>(15, (o1, o2) -> o2 - o1);

    int count = 0;

    public void Insert(Integer num) {

        count++;
        if (max.isEmpty()) {
            max.add(num);
            return;
        }
        if ((count & 1) == 1) {
            if (min.peek() < num) {
                max.add(min.poll());
                min.add(num);
            } else {
                max.add(num);
            }
        } else {
            if (max.peek() > num) {
                min.add(max.poll());
                max.add(num);
            } else {
                min.add(num);
            }
        }
    }

    public Double GetMedian() {

        return (count & 1) == 1 ? Double.valueOf(max.peek()) : (min.peek() + max.peek()) / 2.0 ;
    }


}
