import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String first = br.readLine();
        String second = br.readLine();
        int summary = 0;
        int ft = 0;

        for(int i = 2; i>=0; i--) {
            char c = second.charAt(i);
            int result = (c - '0') * Integer.parseInt(first);
            System.out.println(result);
            if(ft != 0) {
                ft *= 10;
                summary += result * ft;
            } else {
                summary += result;
                ft += 1;
            }
        }
        System.out.println(summary);
    }
}