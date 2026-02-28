import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int play = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < play; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String firstValue = st.nextToken();

            switch (firstValue) {
                case "push":
                    stack.push(Integer.valueOf(st.nextToken()));
                    break;
                case "pop":
                    if (stack.isEmpty()) {
                        sb.append(-1).append("\n"); 
                    }else {
                        sb.append(stack.pop()).append("\n");
                    }
                    break;
                case "size":
                    sb.append(stack.size()).append("\n");
                    break;
                case "empty":
                    sb.append(stack.isEmpty() ? 1 : 0).append("\n");
                    break;
                case "top":
                    if (stack.isEmpty()) {
                        sb.append(-1).append("\n"); 
                    }else {
                        sb.append(stack.peek()).append("\n");
                    }
                    break;
            }
        }
        System.out.print(sb);
    }
}
