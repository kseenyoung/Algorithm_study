import java.util.*;
import java.io.*;

public class S13549_숨바꼭질3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] board = new int[100001];
        int[] pos = new int[2];  // value, x
        Arrays.fill(board, 100000);

        board[N] = 0;
        int[] first = new int[]{0, N};
        Queue<int[]> que = new ArrayDeque<>();
        que.offer(first);

        while(!que.isEmpty()){
            int[] curr = que.poll();
            int value = curr[0];
            int x = curr[1];
            if(board[x] > value)
                continue;

            if(-1 < x-1 && board[x-1] > value+1){
                board[x-1] = value+1;
                que.offer(new int[]{value+1, x-1});
            }
            if(100001 > x+1 && board[x+1] > value+1){
                board[x+1] = value+1;
                que.offer(new int[]{value+1, x+1});
            }
            if(100001 > x*2 && board[x*2] > value){
                board[x*2] = value;
                que.offer(new int[]{value, x*2});
            }
        }

//        sb.append(Arrays.toString(board));
        sb.append(board[K]);
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

}
