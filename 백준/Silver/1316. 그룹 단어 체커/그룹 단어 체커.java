import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (check(br.readLine())) {
                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean check(String str) {
        boolean[] alphabet = new boolean[26];
        int prev = -1;

        for (int i = 0; i < str.length(); i++) {
            int now = str.charAt(i);

            if (prev != now) {
                if (alphabet[now - 'a']) {
                    return false;
                }
                alphabet[now - 'a'] = true;
                prev = now;
            }
        }
        return true;
    }
}
