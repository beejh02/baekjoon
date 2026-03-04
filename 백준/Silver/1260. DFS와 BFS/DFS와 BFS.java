import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {
    static int n, m, v;
    static int[][] arr;
    static boolean[] visited;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        arr = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            arr[start - 1][end - 1] = 1;
            arr[end - 1][start - 1] = 1;
        }

        dfs(v - 1);
        Arrays.fill(visited, false);
        System.out.print("\n");
        bfs(v - 1);

    }

    public static void dfs(int node) {
        visited[node] = true;
        System.out.print(node + 1 + " ");

        for (int i = 0; i < n; i++) {
            if (arr[node][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int node) {
        Deque<Integer> queue = new ArrayDeque<>();
        visited[node] = true;
        queue.add(node);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            System.out.print((current + 1) + " ");

            for (int i = 0; i < n; i++) {
                if (arr[current][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

    }

}
