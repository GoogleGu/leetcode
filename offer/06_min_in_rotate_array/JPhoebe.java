/**
 * 思路:
 * 缩小范围
 * !!!!!!!注意审题：是非减序，没说不能相同
 * !!!!!!!注意审题：是非减序，没说不能相同
 * !!!!!!!注意审题：是非减序，没说不能相同
 * 递归 版
 */
private int minNumberInRotateArray(int[] array) {

    int length = array.length;
    if (length == 0) {
        return 0;
    }
    if (length == 1) {
        return array[0];
    } else if (length == 2) {
        return Math.min(array[0], array[1]);
    }
    int midIndex = (length - 1) / 2;
    // 正序
    if (array[midIndex] > array[0] && array[midIndex] < array[length - 1]) {
        return array[0];
    }
    // 倒叙
    if (array[midIndex] < array[0] && array[midIndex] > array[length - 1]) {
        return array[length - 1];
    }
    // 三点相同
    if (array[midIndex] == array[0] && array[midIndex] == array[length - 1]) {
        // 舍弃最后一位
        // 问题：如果数据全部相同 todo
        this.minNumberInRotateArray(Arrays.copyOfRange(array, 0, length - 2));
    }
    // 前两点相同
    if (array[midIndex] == array[0] && array[midIndex] != array[length - 1]) {
        this.minNumberInRotateArray(Arrays.copyOfRange(array, midIndex + 1, length));
    }
    // 后两点相同
    if (array[midIndex] != array[0] && array[midIndex] == array[length - 1]) {
        this.minNumberInRotateArray(Arrays.copyOfRange(array, 0, midIndex + 1));
    }
    // 正常情况
    if (array[midIndex] < array[0]) {
        this.minNumberInRotateArray(Arrays.copyOfRange(array, 0, midIndex + 1));
    } else {
        this.minNumberInRotateArray(Arrays.copyOfRange(array, midIndex + 1, length));
    }

    return 0;

}

/**
 * 在线编译器不能使用递归，改写for可执行版本
 */
private int method2(int[] array) {

    while (true) {

        int length = array.length;
        if (length == 0) {
            return 0;
        }
        if (length == 1) {
            return array[0];
        } else if (length == 2) {
            return Math.min(array[0], array[1]);
        }
        int midIndex = (length - 1) / 2;
        // 正序
        if (array[midIndex] > array[0] && array[midIndex] < array[length - 1]) {
            return array[0];
        }
        // 倒叙
        if (array[midIndex] < array[0] && array[midIndex] > array[length - 1]) {
            return array[length - 1];
        }
        // 三点相同
        if (array[midIndex] == array[0] && array[midIndex] == array[length - 1]) {
            // 舍弃最后一位
            // 问题：如果数据全部相同 todo
            array = Arrays.copyOfRange(array, 0, length - 2);
            continue;
        }
        // 前两点相同
        if (array[midIndex] == array[0] && array[midIndex] != array[length - 1]) {
            array = Arrays.copyOfRange(array, midIndex + 1, length);
            continue;
        }
        // 后两点相同
        if (array[midIndex] != array[0] && array[midIndex] == array[length - 1]) {
            array = Arrays.copyOfRange(array, 0, midIndex + 1);
            continue;
        }
        // 正常情况
        if (array[midIndex] < array[0]) {
            array = Arrays.copyOfRange(array, 0, midIndex + 1);
            continue;
        } else {
            array = Arrays.copyOfRange(array, midIndex + 1, length);
            continue;
        }

    }

}
