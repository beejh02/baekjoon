import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] numlist = new int[n];

        for(int i = 0; i<n; i++) {
            numlist[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numlist);
        System.out.print(numlist[0] + " " + numlist[n-1]);

    }
}