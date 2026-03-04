import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<String> hashset = new HashSet<>();

        int play = Integer.parseInt(br.readLine());

        for (int i = 0; i < play; i++) {
            hashset.add(br.readLine());
        }
        List<String> arr = new ArrayList<>(hashset);
        arr.sort((s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            }
            return s1.length() - s2.length();
        });

        for (String item : arr) {
            System.out.println(item);
        }
    }
}
