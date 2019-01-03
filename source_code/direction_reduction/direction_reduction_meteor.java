package direction_reduction;

/**
 * @description:
 * @author: Meteor
 * @date: 2018/12/26
 */
public class direction_reduction_meteor {
    public static void main(String[] args) {
        String[] arr = {"NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"};
        for (int i = 0; i < dirReduc(arr).length; i++) {
            System.out.println(dirReduc(arr)[i]);
        }
    }

    public static String[] dirReduc(String[] arr) {
        // Your code here.
        int[] result = new int[arr.length];
        for (int j = 0; j < result.length; j++) {
            result[j] = 1;
        }
        for (int i = 0; i < arr.length; i++) {
            result = iteration(arr,result);
        }
        int count = 0;
        for (int j = 0; j < result.length; j++) {
            if (result[j] == 1) {
                count++;
            }
        }
        int frequency = 0;
        String[] resultStr = new String[count];
        for (int j = 0; j < result.length; j++) {
            if (result[j] == 1) {
                resultStr[frequency] = arr[j];
                frequency++;
            }
        }
        return resultStr;
    }

    public static int[] iteration(String[] arr, int[] result) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (result[i] == 1) {
                int j = i + 1;
                while (j < arr.length - 1 && result[j] != 1 ) {
                    j++;
                }
                switch (arr[i]) {
                    case "NORTH":
                        if (arr[j].equals("SOUTH") && result[j] == 1) {
                            result[i] = result[j] = 0;
                            i++;
                        }
                        break;
                    case "SOUTH":
                        if (arr[j].equals("NORTH") && result[j] == 1) {
                            result[i] = result[j] = 0;
                            i++;
                        }
                        break;
                    case "EAST":
                        if (arr[j].equals("WEST") && result[j] == 1) {
                            result[i] = result[j] = 0;
                            i++;
                        }
                        break;
                    case "WEST":
                        if (arr[j].equals("EAST") && result[j] == 1) {
                            result[i] = result[j] = 0;
                            i++;
                        }
                        break;
                    default:
                        break;
                }
            }
        }
        return result;
    }
}
