import java.io.*;
import java.util.*;

public class Main12919 {

    public static void main(String args[]) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String S=br.readLine();
        String T=br.readLine();
        int s=0, e=T.length()-1, d=1;
        int result=0;
        Queue<int[]> q=new ArrayDeque<>();
        q.offer(new int[]{s,e,d});
        while(!q.isEmpty()){
            int[] cur=q.poll();
            s=cur[0]; e=cur[1]; d=cur[2];
            if(getCurSize(s,e,d)==S.length()){
                if(checkEqual(S, T, s, e, d)){
                    result=1;
                    break;
                } else{
                    continue;
                }
            }
//            System.out.println(s+"/"+e+"/"+d);
            if(T.charAt(e)=='A'){
                q.offer(new int[]{s,e-d,d}); //뒤에만 빠짐
            }
            if(T.charAt(s)=='B'){
                q.offer(new int[]{e,s+d,-d}); //
            }
        }
        System.out.println(result);

    }

    static int getCurSize(int s, int e, int d){
        return (e-s)*d+1; // 5-3+1=3  || -(3-5)+1=3
    }

    static boolean checkEqual(String S, String T, int s, int e, int d){
        int n=S.length();
        int m=(e-s)*d+1;
        if(n!=m) return false;
        for(int i=0;i<n;i++){
            if(S.charAt(i)!=T.charAt(s)) return false;
            s+=d;
        }
        return true;
    }
}
