import java.util.ArrayList;
public class SolutionZcsh {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {

        ArrayList<Integer> result = new ArrayList<>(2);
        int product = Integer.MAX_VALUE;
        for (int i = 0; i < array.length; i++) {
            if (array[i] > sum / 2) {
                break;
            }

            for (int j = i + 1; j < array.length; j++) {
                if (array[i] + array[j] > sum) {
                    break;
                }

                if (array[i] + array[j] == sum && array[i] * array[j] < product) {
                    result.clear();
                    product = array[i] * array[j];
                    result.add(array[i]);
                    result.add(array[j]);
                }
            }
        }



        return result;
    }

}
