import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int play = Integer.parseInt(br.readLine());

        for(int i = 0; i < play; i++) {
            StringBuilder sb = new StringBuilder();

            StringTokenizer st = new StringTokenizer(br.readLine());
            int multiplication = Integer.parseInt(st.nextToken());
            String value = st.nextToken();

            for (int j = 0; j < value.length(); j++) {
            String charStr = String.valueOf(value.charAt(j));
            sb.append(charStr.repeat(multiplication));
        }
        System.out.println(sb.toString());

        }
    }
}