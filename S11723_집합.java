import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class S11723_집합 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int num = 0;

        int bit = 0;

        int Test = Integer.parseInt(br.readLine());
        for(int i=0; i<Test; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String od = st.nextToken();
            switch (od){
                case "add":
                    num = Integer.parseInt(st.nextToken());
                    bit = bit | (1 << num);
                    break;
                case "check":
                    num = Integer.parseInt(st.nextToken());
                    if((bit & (1 << num)) != 0)
                        sb.append(1).append("\n");
                    else
                        sb.append(0).append("\n");
                    break;
                case "remove":
                    num = Integer.parseInt(st.nextToken());
                    bit = bit & ~( 1 << num);
                    break;
                case "toggle":
                    num = Integer.parseInt(st.nextToken());
                    bit = bit ^ (1 << num);
                    break;
                case "all":
                    bit = bit | (~0);
                    break;
                case "empty":
                    bit = 0;
                    break;
            }

        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}
