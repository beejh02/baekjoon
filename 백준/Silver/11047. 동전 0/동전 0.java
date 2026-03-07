import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int play = Integer.parseInt(st.nextToken());
        int goal = Integer.parseInt(st.nextToken());

        int[] arr = new int[play];
        for (int i = 0; i < play; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(counting(play, goal, arr));
    }

    public static int counting(int capacity, int value, int[] array) {
        int count = 0;
        for (int i = capacity - 1; i >= 0; i--) {
            if (array[i] <= value) {
                count += (value / array[i]);
                value %= array[i];
            }
        }
        return count;
    }
}
