import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*Pascal's triangle is a triangular array of integers constructed with the following formula:
The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
Given an input k, return the kth row of Pascal's triangle.*/
public class PascalTriangle {
    static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int k = scan.nextInt();
        List<Integer> lastRow = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j != 0) {
                    try {
                        row.add(lastRow.get(j - 1) + (int) lastRow.get(j));
                    } catch (Exception e) {
                        row.add(1);
                    }
                } else
                    row.add(1);
            }
            lastRow.clear();
            lastRow.addAll(row);
        }
        System.out.println(lastRow);
    }
}
