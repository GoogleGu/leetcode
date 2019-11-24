import java.util.ArrayDeque;
import java.util.ArrayList;

public class SolutionZcsh {


    public ArrayList<Integer> maxInWindows(int[] num, int size) {
        if (size == 0 || num == null || num.length == 0) return new ArrayList<>(0);
        ArrayDeque<Integer> indexArray = new ArrayDeque<>(size);
        ArrayList<Integer> result = new ArrayList<>(num.length / size + 1);
        for (int i = 0; i < num.length; i++) {

            while (!indexArray.isEmpty() && num[indexArray.getLast()] < num[i]) indexArray.pollLast();

            if (!indexArray.isEmpty() && i - size == indexArray.getFirst()) indexArray.pollFirst();

            indexArray.add(i);
            if (i >= size - 1) result.add(num[indexArray.getFirst()]);
        }
        return result;
    }

}
