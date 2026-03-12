import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int capacity = Integer.parseInt(br.readLine());

        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < capacity; i++) {
            Integer input = Integer.valueOf(br.readLine());
            if (input.equals(0)) {
                stack.pop();
            } else {
                stack.push(input);
            }
        }

        int summary = 0;
        for (int item : stack) {
            summary += item;
        }

        System.out.println(summary);
    }
}
