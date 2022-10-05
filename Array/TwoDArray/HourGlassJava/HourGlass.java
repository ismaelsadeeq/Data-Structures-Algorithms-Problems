package TwoDArray.HourGlassJava;

import java.util.List;

public class HourGlass {
    public static int hourglassSum(List<List<Integer>> arr) {
        int sum = 0;
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < arr.size() - 2; i++) { // O(n)
            for (int j = 0; j < arr.get(i).size() - 2; j++) { // O(n)
                sum = arr.get(i).get(j) + arr.get(i).get(j + 1) + arr.get(i).get(j + 2) + arr.get(i + 1).get(j + 1)
                        + arr.get(i + 2).get(j) + arr.get(i + 2).get(j + 1) + arr.get(i + 2).get(j + 2);
                maxValue = Math.max(maxValue, sum);
            }
        }

        return maxValue;
    }
}
