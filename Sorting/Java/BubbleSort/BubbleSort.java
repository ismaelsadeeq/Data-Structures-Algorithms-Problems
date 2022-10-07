import java.util.Arrays;

// We keep swapping to keep max element at its right index

public class BubbleSort {
    public static void main(String[] args) {
        int arr[] = {-1,9,-2,3,4,12,0};
        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }
    static void bubbleSort(int[] arr){
        boolean swapped;
        // run the steps n - 1 times
        for (int i = 0; i < arr.length - 1; i++) {
            swapped = false;
            // for each step. max item will come at the last respective index
            for (int j = 1; j <= arr.length - i -1 ; j++) {
                // swap if item is smaller than previous item
                if (arr[j] < arr[j-1]){
                    //swap
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                    swapped = true;
                }
            }
            // if there is no swap for i = 0, then array is sorted
            if(! swapped) {
                break;
            }
        }
    }
}
