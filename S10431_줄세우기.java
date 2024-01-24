import java.util.*;
import java.io.*;

public class S10431_줄세우기 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int Test = Integer.parseInt(br.readLine());
        for(int test=1; test<=Test; test++){
            int answer = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            int[] numbers = new int[20];
            numbers[0] = Integer.parseInt(st.nextToken());

            for(int i=1; i<20; i++){
                int temp = Integer.parseInt(st.nextToken());
                int index = i;
                while(index > 0 && index < 20 && temp < numbers[index-1]){
                    numbers[index] = numbers[index-1];
                    answer++;
                    index--;
                }
                numbers[index] = temp;
            }
            sb.append(test).append(" ").append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}