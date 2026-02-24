import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String first = br.readLine();
        int dataCapacity = Integer.parseInt(first);
        
        // int[] array = new int[dataCapacity];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int summary = 0;
        int nowMax = Integer.MIN_VALUE;

        for(int i=0; i<dataCapacity; i++) {
            int temp = Integer.parseInt(st.nextToken());
            if(nowMax < temp) nowMax = temp;
            summary += temp;
        }

        float middleValue = (summary / nowMax) + (summary % nowMax) / (float)nowMax;

        System.out.println(middleValue*100/dataCapacity);
    }
}