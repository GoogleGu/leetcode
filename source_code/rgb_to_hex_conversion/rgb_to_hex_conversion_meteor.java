package rgb_to_hex_conversion;

/**
 * @description:
 * @author: Meteor
 * @date: 2018/12/26
 */
public class rgb_to_hex_conversion_meteor {
    public static void main(String[] args) {
        System.out.println(binaryConversion(25));
    }

    public static String binaryConversion(Integer data) {
        if (data >= 0) {
            Integer first = data % 16;
            if (first == 0) {
                if (data / 16 < 15) {
                    return outPut((data / 16)) + "0";
                }
            } else {
                Integer second = (data - first) / 16;
                if (second >= 16) {
                    return "FF";
                }
                return outPut(second) + outPut(first);
            }
        }
        return "数据必须大于0！";
    }
    public static String outPut(Integer a) {
        if (a <= 9) {
            return a.toString();
        } else {
            switch (a) {
                case 10:
                    return "A";
                case 11:
                    return "B";
                case 12:
                    return "C";
                case 13:
                    return "D";
                case 14:
                    return "E";
                case 15:
                    return "F";
                default:
                    return "F";
            }
        }
    }
}
