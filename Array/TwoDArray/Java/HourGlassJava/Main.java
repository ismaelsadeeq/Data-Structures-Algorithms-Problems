package TwoDArray.HourGlassJava;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<List<Integer>> arr = new ArrayList<>();
        ArrayList<Integer> firstRow = new ArrayList<>();
        ArrayList<Integer> secondRow = new ArrayList<>();
        ArrayList<Integer> thirdRow = new ArrayList<>();
        ArrayList<Integer> forthRow = new ArrayList<>();
        ArrayList<Integer> fifthRow = new ArrayList<>();
        ArrayList<Integer> sixthRow = new ArrayList<>();
        firstRow.add(1);
        firstRow.add(1);
        firstRow.add(1);
        firstRow.add(0);
        firstRow.add(0);
        firstRow.add(0);
        secondRow.add(0);
        secondRow.add(1);
        secondRow.add(0);
        secondRow.add(0);
        secondRow.add(0);
        secondRow.add(0);

        thirdRow.add(1);
        thirdRow.add(1);
        thirdRow.add(1);
        thirdRow.add(0);
        thirdRow.add(0);
        thirdRow.add(0);
        forthRow.add(0);
        forthRow.add(0);
        forthRow.add(2);
        forthRow.add(4);
        forthRow.add(4);
        forthRow.add(0);

        fifthRow.add(0);
        fifthRow.add(0);
        fifthRow.add(0);
        fifthRow.add(2);
        fifthRow.add(0);
        fifthRow.add(0);
        sixthRow.add(0);
        sixthRow.add(0);
        sixthRow.add(1);
        sixthRow.add(2);
        sixthRow.add(4);
        sixthRow.add(0);
        arr.add(firstRow);
        arr.add(secondRow);
        arr.add(thirdRow);
        arr.add(forthRow);
        arr.add(fifthRow);
        arr.add(sixthRow);
        int result = HourGlass.hourglassSum(arr);
        System.out.println(result);
    }
}
