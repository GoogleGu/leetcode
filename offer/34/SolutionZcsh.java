public class SolutionZcsh {
    private int[] array;

    private final int SHOW_NUMBER_FLAG = 100000;

    public int FirstNotRepeatingChar(String str) {
        array = new int[256];
        char[] chars = str.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            int aChar = chars[i];

            array[aChar] += array[aChar] == 0 ? i + SHOW_NUMBER_FLAG : SHOW_NUMBER_FLAG;
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < array.length; i++) {
            if (array[i] >= SHOW_NUMBER_FLAG && array[i] < 200000 && min > array[i]) {
                min = array[i];
            }
        }

        return min == Integer.MAX_VALUE ? -1 : min - SHOW_NUMBER_FLAG;
    }

}
