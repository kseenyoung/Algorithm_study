import java.util.*;
import java.io.*;

public class S1389_케빈_베이컨의_6단계_법칙 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] adjMatrix = new int[N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                adjMatrix[i][j] = 10000000;
            }
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;
            adjMatrix[a][b] = 1;
            adjMatrix[b][a] = 1;
        }

        for(int k=0; k<N; k++){
            for(int i=0; i<N; i++){
                for(int j=0; j<N; j++){
                    int temp = adjMatrix[i][k] + adjMatrix[k][j];
                    if(adjMatrix[i][j] > temp){
                        adjMatrix[i][j] = temp;
                    }
                }
            }
        }

        // answer
        int answer = N, sum = 10000000;
        for(int i=0; i<N; i++){
            int temp = Arrays.stream(adjMatrix[i]).sum();
            if(sum > temp){
                sum = temp;
                answer = i+1;
            }
        }

        System.out.println(answer);


    }

}
