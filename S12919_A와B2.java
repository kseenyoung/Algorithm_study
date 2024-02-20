import java.io.*;
import java.util.*;

public class S12919_A와B2 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        PriorityQueue<String> que = new PriorityQueue();

        String S = br.readLine(); // S
        que.offer(S);
        String T = br.readLine();  // T
        int Tlength = T.length();
        String A = null, B = null;

        while(!que.isEmpty()){
            String curr = que.poll();
            if(curr.equals(S)){
                System.out.println(1);
                return;
            }

            sb.setLength(0);
            A = sb.append(curr).append("A").toString();
            sb.setLength(0);
            B = sb.append(curr).append("B").reverse().toString();

            sb.setLength(0);
            if(curr.length()+1 == Tlength){
                if(A.equals(T) || B.equals(T)){
                    System.out.println(1);
                    return;
                }
            } else if(curr.length()+1 < Tlength){
                que.offer(A);
                que.offer(B);
            }

        }
        System.out.println(0);

    }

    public static String removeLastString(String str){
        if(str == null || str.isEmpty())
            return str;
        StringBuilder sb = new StringBuilder(str);
//        return sb.deleteCharAt(sb.length() -1);
    }
}
