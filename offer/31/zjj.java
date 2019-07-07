public int NumberOf1Between1AndN_Solution(int n) {
        int num=0;
        for (int i = 0;i<=n;i++){
        String strI = String.valueOf(i);
        for (int j=0;j<strI.length();j++){
        if (strI.substring(j,j+1).equals("1")){
        num++;
        }
        }

        }
        return num;
        }