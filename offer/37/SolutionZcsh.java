public class SolutionZcsh {
    public int GetNumberOfK(int [] array , int k) {
        int index = search(array,0, array.length , k);
        if (index == -1) {
            return 0;
        }
        int sum = 1;
        for (int i = index - 1; i >= 0; i--) {
            if (array[i] == k) {
                sum++;
            }
        }
        for (int i = index + 1; i < array.length; i++) {
            if (array[i] == k) {
                sum++;
            }
        }
        
        return sum;
    }
    
    public int search(int[] array, int left,int rigth, int k) {
        if (left == rigth) {
            return -1;
        }
        int middle = (left + rigth) / 2;
        if (k < array[middle]){
            return search(array, left , middle - 1 , k);
        } else if (k > array[middle]) {
            return search(array, middle + 1, rigth, k);
        } else {
            return middle;
        }
        
    }
}
