import java.io.*;
import java.util.*;
public class S20055_컨베어벨트_위의_로봇 {
    static int countHp=0, result = 0, K;
    static Deque<Kan> up, down;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N  = Integer.parseInt(st.nextToken());
        K  = Integer.parseInt(st.nextToken());

        up = new ArrayDeque<>();
        down = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<2*N; i++){
            Kan kan = new Kan(Integer.parseInt(st.nextToken()));
            if(i < N){
                up.offer(kan);
            } else{
                down.offerFirst(kan);
            }
        }

        while(countHp < K){
            rotation();
            moveRobot();
            setRobot();
            result++;
        }

        bw.write(sb.append(result).toString());
        bw.flush();
        bw.close();

    }

    public static void setRobot(){
        Kan first = up.peek();
        if(first.hp > 0){
            first.isRobot = true;
            first.hp--;
            if(first.hp == 0)
                countHp++;
        }
    }

    public static void rotation(){
        Kan toUp = down.poll();
        if(toUp.isRobot){
            toUp.hp--;
            if(toUp.hp == 0) countHp++;
        }

        Kan toDown = up.pollLast();
        if(toDown.isRobot){
            toDown.hp--;
            if(toDown.hp == 0) countHp++;
        }

        up.offerFirst(toUp);
        down.offerLast(toDown);

        checkDown();
    }

    public static void checkDown(){
        // 내리는 위치 확인
        up.peekLast().isRobot = false;
    }

    public static void moveRobot(){
        Object[] upArray = up.toArray();
        for(int i=up.size()-2; i>=0; i--) {
            Kan from = ((Kan) upArray[i]);
            Kan to = ((Kan) upArray[i + 1]);
            if (from.isRobot && !to.isRobot && to.hp > 0) {
                from.isRobot = false;
                to.isRobot = true;
                to.hp--;
                if (to.hp == 0)
                    countHp++;
            }
        }
        checkDown();
    }
}

class Kan{
    int hp=0;
    boolean isRobot=false;
    Kan(int hp){this.hp = hp;}
}