package ant_bridge;

import java.util.HashSet;
import java.util.Set;

/**
 * @author Dream
 * @date 2018/12/12 19:57
 */
public class AntBridgeDr {

    public static String antBridge(String ants, String terrain) {
        terrain = String.format("-%s-", terrain);
        char[] chars = terrain.toCharArray();
        int keng = 0;
        for (int i = 1; i < chars.length - 1; i++) {
            if (chars[i] == '.' || chars[i - 1] == '.' || chars[i + 1] == '.') {
                keng++;
            }
        }
        int index = keng % ants.length();
        String newAnts = ants.substring(ants.length() - index, ants.length());
        newAnts += ants.substring(0, ants.length() - index);
        return newAnts;
    }

    public static String antBridge2(String ants, String terrain) {
        Set<Integer> keng = new HashSet<>();
        char[] chars = terrain.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '.') {
                keng.add(i);
                if (chars[i - 1] == '-') {
                    keng.add(i - 1);
                }
                if (chars[i + 1] == '-') {
                    keng.add(i + 1);
                }
            }
        }
        int index = keng.size() % ants.length();
        String newAnts = ants.substring(ants.length() - index, ants.length());
        newAnts += ants.substring(0, ants.length() - index);
        return newAnts;
    }
}
