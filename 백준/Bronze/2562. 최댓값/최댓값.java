import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] array = new int[10];

        int nowMax = -1;
        int nowIndex = -1;

        for(int i = 0; i < 9; i++) {
            array[i] = Integer.parseInt(br.readLine());
            if (array[i] > nowMax) {
                nowMax = array[i];
                nowIndex = i+1;
            }
        }

        System.out.println(nowMax);
        System.out.println(nowIndex);
    }
}