import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

class Main {
    public static void main(String args[]) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCapacity = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < inputCapacity; i++) {
            map.put(st.nextToken(), 1);
        }

        int checkCapacity = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < checkCapacity; i++) {
            sb.append(map.getOrDefault(st.nextToken(), 0)).append("\n");
        }

        System.out.print(sb.toString());
    }
}
