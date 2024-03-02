import java.io.*;

public class 쿠키의신체측정 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int hr=-1, hc=-1;
        int[] size=new int[5]; //왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
        String s[]=new String[N];
        for(int i=0;i<N;i++){
            s[i]=br.readLine();
            if(hr<0){
                for(int k=0;k<N;k++){
                    if(s[i].charAt(k)=='*'){
                        hr=i+1;
                        hc=k;
                    }
                }
            }
        }
        //팔
        size[0]=findLeft(s,hr,hc-1);
        size[1]=findRight(s,hr,hc+1);
        //허리
        size[2]=findDown(s,hr+1,hc);
        //다리
        int lr=hr+size[2]+1;
        size[3]=findDown(s,lr,hc-1);
        size[4]=findDown(s,lr,hc+1);

        StringBuilder sb=new StringBuilder();
        sb.append(++hr).append(" ").append(++hc).append("\n");
        for(int x: size){
            sb.append(x).append(" ");
        }
        System.out.println(sb.toString());
    }
    static int findLeft(String[] s, int r, int c){
        int len=0;
        for(int i=c;i>=0;i--){
            if(s[r].charAt(i)!='*'){
                break;
            }
            len++;
        }
        return len;
    }
    static int findRight(String[] s, int r, int c){
        int len=0, n=s.length;
        for(int i=c;i<n;i++){
            if(s[r].charAt(i)!='*'){
                break;
            }
            len++;
        }
        return len;
    }

    static int findDown(String[] s, int r, int c){
        int len=0, n=s.length;
        for(int i=r;i<n;i++){
            if(s[i].charAt(c)!='*'){
                break;
            }
            len++;
        }
        return len;
    }
}
