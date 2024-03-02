import java.io.*;
import java.util.*;
public class 문자열게임20437 {
    public static void main(String[] args) throws IOException {

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        int TC=Integer.parseInt(br.readLine());
        while(TC-->0 ){
            String input= br.readLine();
            int k=Integer.parseInt(br.readLine());
            Map<Character,List<Integer>> dict=new HashMap<>();
            for(int i=0;i<input.length();i++){
                char c=input.charAt(i);
                if(!dict.containsKey(c)){
                    dict.put(c,new ArrayList<>());
                }
                dict.get(c).add(i);
            }
            Set<Character> candidate=new HashSet<>();
            for(char c: dict.keySet()){
                if(dict.get(c).size()>=k){
                    candidate.add(c);
                }
            }
            //만약 k개 넘는 애들이 없다면 -1하고 바로 다음 걸로
            if(candidate.isEmpty()){
                sb.append(-1).append("\n");
                continue;
            }
            //있다면
            //k개 이상 가진 애들 사이에서...정확히 k개를 가진 경우 구하기! -> 최대 최소 저장하기!
            int min=input.length(), max=k;
            for(char c: candidate){
                List<Integer> cur=dict.get(c);
                int n=cur.size(), num=n-k+1;
                for(int i=0;i<num;i++){
                    int tmp=cur.get(i+k-1)-cur.get(i)+1;
                    if(tmp>max) max=tmp;
                    if(tmp<min) min=tmp;
                }
            }
            sb.append(min).append(" ").append(max).append("\n");
        }
        System.out.print(sb.toString());
    }
}
