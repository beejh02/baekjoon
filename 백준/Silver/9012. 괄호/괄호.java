import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int play = Integer.parseInt(br.readLine());

        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < play; i++) {
            String value = br.readLine();
            for(int j = 0; j < value.length(); j++) {
                char temp = value.charAt(j);
                if(temp == '(') stack.push(temp);
                else if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                }else {
                    stack.push(temp);
                }
            }

            if(stack.isEmpty()) {
                System.out.println("YES");
            } else{
                System.out.println("NO");
            }

            stack.clear();
        }
    }
}