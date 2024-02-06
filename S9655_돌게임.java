import java.util.*;
import java.io.*;

public class S9655_돌게임 {

    static Queue<int[]> que;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] game = new int[N+1];
        game[0] = 2;
        // 1 SK, 2 CY
        que = new ArrayDeque();
        que.offer(new int[]{2, 0});  // 누구, 위치

        while(!que.isEmpty()){
            int[] curr = que.poll();
            int who = curr[0];
            int pos = curr[1];

            game[pos] = who;
            if(who == 1){
                setGame(game, 2, pos);
            } else{
                setGame(game, 1, pos);
            }
        }

        String result = null;
        if(game[N] == 1)
            result = "SK";
        else
            result = "CY";

        bw.write(result);
        bw.flush();
        bw.close();

    }

    public static void setGame(int[] game, int who, int pos){
        if(game.length > pos+1 && game[pos+1] == 0){
            game[pos+1] = who;
            que.offer(new int[]{who, pos+1});
        }
        if(game.length > pos+3 && game[pos+3] == 0){
            game[pos+3] = who;
            que.offer(new int[]{who, pos+3});
        }
    }
}
