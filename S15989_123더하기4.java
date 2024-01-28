import java.util.*;
import java.io.*;

public class S15989_123더하기4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int[][] nums = new int[10001][4];
        nums[1][1] = 1;
        nums[2][1] = 1;
        nums[2][2] = 1;
        nums[3][1] = 1;
        nums[3][2] = 1;
        nums[3][3] = 1;

        for(int i=4; i<=10000; i++){
            nums[i][1] = nums[i-1][1];
            nums[i][2] = nums[i-2][1] + nums[i-2][2];
            nums[i][3] = nums[i-3][1] + nums[i-3][2] + nums[i-3][3];
        }

        int Test = Integer.parseInt(br.readLine());
        for(int test=1; test<=Test; test++){
            int N = Integer.parseInt(br.readLine());
                sb.append(nums[N][1] + nums[N][2] + nums[N][3]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
