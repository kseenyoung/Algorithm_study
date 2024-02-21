import java.io.*;

public class Main2292 {
    public static void main(String[] args) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int k=1, res=1;
        while(k<n){
            k+=res*6;
            res++;
        }
        System.out.println(res);
    }
}
