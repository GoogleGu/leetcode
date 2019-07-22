public int GetUglyNumber_Solution(int index) {
        if (index<=0){
        return 0;
        }
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(1);
        int b2=0,b3=0,b5 =0;
        for (int i=1;i<index;i++){
        list.add(i,Math.min(list.get(b2)*2,Math.min(list.get(b3)*3,list.get(b5)*5)));
        if (list.get(i)==list.get(b2)* 2){
        b2 ++;
        }
        if (list.get(i)==list.get(b3)*3){
        b3 ++;
        }
        if (list.get(i)==list.get(b5)* 5){
        b5 ++;
        }
        }

        return list.get(index -1);
        }