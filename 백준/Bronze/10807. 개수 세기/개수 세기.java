import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int capacity = Integer.parseInt(br.readLine());
        int[] arr = new int[capacity];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < capacity; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int value = Integer.parseInt(br.readLine());
        int count = 0;

        for (int item : arr) {
            if (value == item) {
                count++;
            }
        }

        System.out.println(count);

    }
}
