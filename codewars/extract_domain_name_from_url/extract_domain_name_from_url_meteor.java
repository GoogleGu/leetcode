package extract_domain_name_from_url;

/**
 * @description:
 * @author: Meteor
 * @date: 2019/1/3
 */
public class extract_domain_name_from_url_meteor {
    public static void main(String[] args) {
        String URl = "https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python";
        String[] result = URl.split("\\.");
        if (result.length > 2) {
            System.out.println(result[1]);
        } else {
            String[] resultFinaly = result[0].split("/");
            System.out.println(resultFinaly[2]);
        }
    }
}
