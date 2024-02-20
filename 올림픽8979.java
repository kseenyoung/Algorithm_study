import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 올림픽8979 {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<int[]> pq=new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[1]==o2[1]){
                    if(o1[2]==o2[2]){
                        return o2[3]-o1[3];
                    }
                    return o2[2]-o1[2];
                }
                return o2[1]-o1[1];
            }
        });
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            int id=Integer.parseInt(st.nextToken());
            int g=Integer.parseInt(st.nextToken());
            int s=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            pq.offer(new int[]{id,g,s,b});
        }
        int rank=0, next=1;
        int[] prev={0,-1,-1,-1};
        while(!pq.isEmpty()){
            int[] cur=pq.poll();
            if(prev[1]==cur[1] && prev[2]==cur[2] && prev[3]==cur[3]){
                next++;
            } else{
                rank+=next;
                next=1;
            }
            if(cur[0]==k){
                System.out.println(rank);
                break;
            }
            prev=cur;
        }
    }
}
