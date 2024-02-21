import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Solution10431 {

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int P=Integer.parseInt(st.nextToken());
        for(int i=1;i<=P;i++){
            st=new StringTokenizer(br.readLine());
            st.nextToken();
            int res=0;
            List<Integer> order=new LinkedList<>();
            order.add(Integer.parseInt(st.nextToken()));
            for(int j=0;j<19;j++){
                int k=Integer.parseInt(st.nextToken());
                int tmp=0;
                for(int t=j;t>=0;t--){
                    if(order.get(t)<k){
                        order.add(t+1,k);
                        break;
                    }
                    tmp++;
                }
                if(order.size()-1==j){
                    order.add(0,k);
                }
                res+=tmp;
            }
            System.out.println(i+" "+res);
        }
    }
}
