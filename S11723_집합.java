import java.util.*;
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class S11723_집합 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        Set<Integer> set = new HashSet<>();
        int num = 0;

        Stream<Integer> stream;

        int Test = Integer.parseInt(br.readLine());
        for(int i=0; i<Test; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String od = st.nextToken();
            switch (od){
                case "add":
                    num = Integer.parseInt(st.nextToken());
                    set.add(num);
                    break;
                case "check":
                    num = Integer.parseInt(st.nextToken());
                    if(set.contains(num))
                        sb.append(1).append("\n");
                    else
                        sb.append(0).append("\n");
                    break;
                case "remove":
                    num = Integer.parseInt(st.nextToken());
                    set.remove(num);
                    break;
                case "toggle":
                    num = Integer.parseInt(st.nextToken());
                    if(set.contains(num))
                        set.remove(num);
                    else
                        set.add(num);
                    break;
                case "all":
                    stream = Stream.iterate(1, n -> n+1).limit(20);
                    set = new HashSet<>(stream.collect(Collectors.toList()));
                    break;
                case "empty":
                    set = new HashSet<>();
                    break;
            }

        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}
