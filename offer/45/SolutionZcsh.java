import java.util.HashSet;
public class SolutionZcsh {
    public boolean isContinuous(int [] numbers) {

        if (numbers == null || numbers.length < 5) {
            return false;
        }

        int min = 15;
        int max = -1;
        HashSet<Integer> collections = new HashSet<>();
        int zero = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < min && numbers[i] != 0)  {
                min = numbers[i];
            }
            if (numbers[i] > max) {
                max = numbers[i];
            }
            if (numbers[i] == 0) {
                zero++;
            } else {
                collections.add(numbers[i]);
            }
        }
        
        return max - min <= 4 && zero + collections.size() == 5;

    }
}
