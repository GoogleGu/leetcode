public String ReverseSentence(String str){
        if (str==null||str.trim().equals("")){
        return str;
        }
        StringBuffer stringBuffer = new StringBuffer();
        String[] words = str.split(" ");
        for (int i=words.length-1;i>=0;i--){
        stringBuffer.append(words[i]);
        stringBuffer.append(" ");
        }
        stringBuffer.deleteCharAt(stringBuffer.length()-1);
        return stringBuffer.toString();
        }