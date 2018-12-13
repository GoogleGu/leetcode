package ant_bridge;

/**
 * @description:
 * @author: Meteor
 * @date: 2018/12/11
 */
public class ant_bridge_meteor {

    public static void main(String[] args) {
        String ants = "DCBA";
        String terrain = "---.----..------.---";
        System.out.println(antBridge(ants,terrain));
    }

    public static String antBridge(final String ants, final String terrain) {
        // Your code here!
        final char gap = ".".charAt(0);
        final char ground = "-".charAt(0);
        String result = null;
        StringBuilder ant = new StringBuilder();
        ant.append(ants);
        char[] terrains = terrain.toCharArray();
        int count = 0;
        for (int i = 1; i < terrains.length-1; i++) {
            if (terrains[i] == gap) {
                if (terrains[i - 1] != gap) {
                    terrains[i - 1] = gap;
                }
                if (terrains[i + 1] != gap) {
                    terrains[i + 1] = gap;
                    i++;
                }
            }
        }
        for (int i = 0; i < terrains.length; i++) {
            System.out.print(terrains[i]);
            if (terrains[i] == gap) {
                count++;
            }
        }
        result  = crossTheBridge(count % ants.length(),ant);
        return result;
    }
    public static String crossTheBridge(int count, StringBuilder ants) {
        String ant = ants.substring(0,ants.length() - count);
        ants.delete(0,ants.length() - count);
        ants.append(ant);
        return ants.toString();
    }
}
