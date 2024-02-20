import java.io.*;
import java.util.*;

public class S10431_줄세우기Re {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb =  new StringBuilder();

        int P = Integer.parseInt(br.readLine());
        for(int test=1; test<=P; test++){
            int result = 0;
            int cnt = 0, curr = 0, index = 0;
            int[] students = new int[20];

            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken(); // test

            for(int i=0; i<20; i++){
                curr = Integer.parseInt(st.nextToken());
                index = i;
                while(index-1 >= 0 && students[index-1] > curr){
                    students[index] = students[index-1];
                    index--;
                    cnt++;
                }
                students[index] = curr;
                result = cnt;
            }
            sb.append(test).append(" ").append(result).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}
