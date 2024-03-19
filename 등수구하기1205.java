import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 등수구하기1205 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int s=Integer.parseInt(st.nextToken());
        int p=Integer.parseInt(st.nextToken());
        if(n==0) {
            System.out.println(1);
            return;
        }

        st=new StringTokenizer(br.readLine());
        int[] arr=new int[n+1];
        for(int i=1;i<=n;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }
//        System.out.println(Arrays.toString(arr));
        if(n<p){
            for(int i=1;i<=n;i++){
                if(arr[i]<=s){
                    System.out.println(i);
                    return;
                }
            }
            if(arr[n]>s) System.out.println(n+1);
            else System.out.println(n);
        }else{
            if(arr[p]>=s){
                System.out.println(-1);
                return;
            }
            for(int i=p-1;i>0;i--){
                if(arr[i]>s){
                    System.out.println(i+1);
                    return;
                }
            }
            System.out.println(1);
        }

    }
}
