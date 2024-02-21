import java.io.*;
import java.util.*;

public class S12919_A와B2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        PriorityQueue<String> que = new PriorityQueue();

        String S = br.readLine(); // S
        String T = br.readLine();  // T
        que.offer(T);
        int Slength = S.length();
        String A = null, B = null;

        while (!que.isEmpty()) {
            String curr = que.poll();
            if (curr.equals(S)) {
                System.out.println(1);
                return;
            }
            String temp = null;

            if (curr.length() > 1 && curr.charAt(curr.length() - 1) == 'A') {
                temp = removeLastString(curr);
                if (temp.equals(S)) {
                    System.out.println(1);
                    return;
                }
                que.offer(temp);
            }
            if (curr.length() > 1 && curr.charAt(0) == 'B') {
                temp = removeAndReverseString(curr);
                if (temp.equals(S)) {
                    System.out.println(1);
                    return;
                }
                que.offer(temp);
            }

        }
        System.out.println(0);

    }

    public static String removeLastString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        StringBuilder sb = new StringBuilder(str);
        return sb.deleteCharAt(sb.length() - 1).toString();
    }

    public static String removeAndReverseString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        StringBuilder sb = new StringBuilder(str);
        return sb.deleteCharAt(0).reverse().toString();
    }
}
