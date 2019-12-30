package rgb_to_hex_conversion;

import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * @author Dream
 * @date 2018/12/24 19:52
 */
public class RGBToHexConversionDr {
    private static String rgb(int r, int g, int b) {
        return Arrays.asList(r, g, b).stream().map(i -> Integer.toHexString(i < 0 ? 0 : i > 255 ? 255 : i)).collect(Collectors.joining());
    }
}
