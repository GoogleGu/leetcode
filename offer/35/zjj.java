

//在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

public int InversePairs(int [] array) {
        int num = array.length;
        if (array==null||num==0){
        return 0;
        }
        int[] copy = array.clone();
        int count = count(array,copy,0,num-1);
        return count;
        }

public int count(int[] array,int[] copy,int low,int high){
        int Y =1000000007;
        if (low==high){
        return 0;
        }
//        int mid = (low+high)>>1;
        int mid = (low+high)/2;
        int leftCount = count(array,copy,low,mid)%Y;
        int rightCount = count(array,copy,mid+1,high)%Y;
        int count =0;
        int i = mid;
        int j = high;
        int locCopy = high;
        while (i>=low&&j>mid){
        if (array[i]>array[j]){
        count = count +j-mid;
        copy[locCopy--] = array[i--];
        if (count>=Y){
        count = count%Y;
        }
        }else {
        copy[locCopy--] = array[j--];
        }
        }
        while (i>=low){
        copy[locCopy--]=array[i];
        i--;
        }
        while (j>mid){
        copy[locCopy--]=array[j];
        j--;
        }
        for (int s =low;s<=high;s++){
        array[s] = copy[s];
        }

        return (leftCount+rightCount+count)%Y;
        }