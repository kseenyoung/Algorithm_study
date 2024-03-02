import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 덩치 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        Man[] men=new Man[n];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            int kg=Integer.parseInt(st.nextToken());
            int cm=Integer.parseInt(st.nextToken());
            men[i]=new Man(kg,cm);
        }
        for(int i=0;i<n;i++){
            Man cur=men[i];
            for(int j=i+1;j<n;j++){
                Man tmp=men[j];
                int check=cur.compareTo(tmp);
                if(check<0){ //내가 더 큰 경우
                    tmp.rankDown(1);
                }else{
                    cur.rankDown(check);
                }
            }
        }
        StringBuilder sb=new StringBuilder();
        for(Man m:men){
            sb.append(m.rank).append(" ");
        }
        System.out.println(sb.toString());
    }

    static class Man implements Comparable<Man>{
        int kg, cm, rank;

        Man(int kg,int cm){
            this.kg=kg;
            this.cm=cm;
            rank=1;
        }

        void rankDown(int rank){
            this.rank+=rank;
        }

        @Override
        public int compareTo(Man o) {
            if(this.kg<o.kg && this.cm<o.cm){
                return 1;
            } else if (this.kg>o.kg && this.cm>o.cm) {
                return -1;
            }
            return 0;
        }
    }
}
