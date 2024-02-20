import java.util.*;
import java.io.*;

public class S2292_벌집 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int curr = 2, index =1;
        // 1 : 1
        // 2 : 2 ~ 7(6)
        // 3 : 8 ~ 19(12)
        // 4 : 20 ~ 37(18)
        // 5 : 38 ~ 61(23)
        if(N == 1) System.out.println(1);
        else{
            while(curr <= N){
                curr += index++*6;
            }
            System.out.println(index);
        }

    }
}
