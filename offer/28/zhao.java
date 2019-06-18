

public int operation(int [] array){

    int len = array.length; // 数组总长度
    int index=len; // 满足条件的下标
    int[] num = new int[len]; // /存放次数的数组

    for (int i = 0;i<=len-1;i++){
        for (int j = 0;j<=len-1;j++){
            if (array[i]==array[j]){
                num[i]++;
                if (num[i]>len/2){
                    index = i;
                    return array[i];
                }
            }
        }
    }

    if (index==len){
        return 0;
    }else {
        return array[index];
    }
}