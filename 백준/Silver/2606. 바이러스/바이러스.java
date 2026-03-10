import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int vertexCnt;
    static int edgeCnt;
    static int[][] arr;
    static boolean[] visited;
    static int cnt;

    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        vertexCnt = Integer.parseInt(br.readLine());
        edgeCnt = Integer.parseInt(br.readLine());
        arr = new int[vertexCnt][vertexCnt];
        visited = new boolean[vertexCnt];
        cnt = 0;

        for (int i = 0; i < edgeCnt; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;

            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        dfs(0);
        System.out.println(cnt);
    }

    public static void dfs(int index) {
        visited[index] = true;
        for (int i = 0; i < vertexCnt; i++) {
            if (arr[index][i] == 1 && !visited[i]) {
                cnt++;
                dfs(i);
            }
        }
    }
}
