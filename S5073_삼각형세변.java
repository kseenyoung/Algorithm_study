import java.util.*;
import java.io.*;

public class S5073_삼각형세변 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        while(true){
            StringTokenizer st =new StringTokenizer(br.readLine());
            int[] nums = new int[3];
            nums[0] = Integer.parseInt(st.nextToken());
            nums[1] = Integer.parseInt(st.nextToken());
            nums[2] = Integer.parseInt(st.nextToken());

            if(nums[0] == 0 && nums[1] == 0 && nums[2] == 0)
                break;

            Arrays.sort(nums);

            if(nums[0] == nums[1] && nums[1] == nums[2]){
                sb.append("Equilateral").append("\n");
            } else if((nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2]) && nums[2] < nums[0] + nums[1]){
                sb.append("Isosceles").append("\n");
            } else if(nums[2] < nums[0] + nums[1]){
                sb.append("Scalene").append("\n");
            } else{
                sb.append("Invalid").append("\n");
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}
