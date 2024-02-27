import java.io.*;
import java.util.*;

public class 컨베이어벨트위의로봇20055 {

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int n=Integer.parseInt(st.nextToken());
        int NUM=n*2;
        int k=Integer.parseInt(st.nextToken());

        st=new StringTokenizer(br.readLine());
        int[] block=new int[NUM];
        int[] robot=new int[NUM];
        for(int i=0;i<NUM;i++){
            block[i]=Integer.parseInt(st.nextToken());
        }
        int cur=0, step=0;
        while (k>0) {
//            System.out.println(step+": cur "+cur);
//            System.out.println(Arrays.toString(block));
//            System.out.println(Arrays.toString(robot));
            step++;
            //1. 회전
            cur -= 1;
            if (cur < 0) cur += NUM;
            //2. 이동
            int down = (cur + n-1) % NUM;
            //2-1. 내려가기
            if (robot[down] == 1) {
                robot[down] = 0;
            }
            for (int i = 0; i < n - 1; i++) {
                int ci = (down - i+NUM)%NUM;
                int bi = (down - i-1+NUM)%NUM;
                if (robot[ci] == 0 && block[ci] > 0 && robot[bi] == 1) {
                    robot[ci] = 1;
                    robot[bi] = 0;
                    if (--block[ci] == 0) {
                        k--;
                    }
                }
            }
            //움직여서 바로 내려갈 준비된 애들 내리기
            if (robot[down] == 1) {
                robot[down] = 0;
            }
            //3. 올리기
            if (block[cur] > 0) {
                robot[cur] = 1;
                if (--block[cur] == 0) {
                    k--;
                }
            }
        }
        System.out.println(step);
    }

}
