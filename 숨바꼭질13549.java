import java.io.*;
import java.util.*;

public class 숨바꼭질13549 {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        int L=100_000;
        if(k<=n){
            System.out.println(n-k);
        }else{
            Queue<Integer> q=new ArrayDeque();
            Map<Integer,Integer> visited=new HashMap<>();
            q.offer(n);
            visited.put(n,0);
            while (!q.isEmpty()){
                int loc=q.poll();
                int dist=visited.get(loc);
                if(loc==k){
                    System.out.println(dist);
                    break;
                }
                if(visited.containsKey(loc*2)){
                    if (visited.get(loc*2)>dist){
                        q.offer(loc*2);
                        visited.put(loc*2,dist);
                    }
                } else if(loc*2<=L){
                    q.offer(loc*2);
                    visited.put(loc*2,dist);
                }

                if(visited.containsKey(loc+1)){
                    if (visited.get(loc+1)>dist+1){
                        q.offer(loc+1);
                        visited.put(loc+1,dist+1);
                    }
                } else if(loc+1<=L){
                    q.offer(loc+1);
                    visited.put(loc+1,dist+1);
                }

                if(visited.containsKey(loc-1)){
                    if (visited.get(loc-1)>dist+1){
                        q.offer(loc-1);
                        visited.put(loc-1,dist+1);
                    }
                } else if(loc>0){
                    q.offer(loc-1);
                    visited.put(loc-1,dist+1);
                }
            }
        }
    }
}
