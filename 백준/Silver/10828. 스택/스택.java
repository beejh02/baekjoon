
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

class Main {
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int play = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < play; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String firstValue = st.nextToken();

            switch (firstValue) {
                case "push" ->
                    stack.push(Integer.valueOf(st.nextToken()));
                case "top" -> {
                    if (stack.empty()) {
                        System.out.println(-1); 
                    }else {
                        System.out.println(stack.peek());
                    }
                }
                case "empty" -> {
                    if (stack.empty()) {
                        System.out.println(1); 
                    }else {
                        System.out.println(0);
                    }
                }
                case "pop" -> {
                    if (stack.empty()) {
                        System.out.println(-1); 
                    }else {
                        System.out.println(stack.pop());
                    }
                }
                case "size" -> {
                    System.out.println(stack.size());
                }
                default -> {
                }
            }
        }

    }
}
