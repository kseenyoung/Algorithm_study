import java.util.*;
import java.io.*;

public class S23971_ZOAC4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int i=0, j=0, answer=0;

        while(true){
            if(j >= W){
                j = 0;
                i += N+1;
            }
            if(i >= H)
                break;
            answer += 1;
            j += M+1;
        }

        System.out.print(answer);

    }
}
