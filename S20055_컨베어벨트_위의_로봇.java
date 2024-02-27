import java.io.*;
import java.util.*;
public class S20055_컨베어벨트_위의_로봇 {
    static int countRobot = 0;
    static Deque<Kan> up, down;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N  = Integer.parseInt(st.nextToken());
        int K  = Integer.parseInt(st.nextToken());

        up = new ArrayDeque<>();
        down = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            Kan kan = new Kan(Integer.parseInt(st.nextToken()));
            if(i < N){
                up.add(kan);
            } else{
                down.add(kan);
            }
        }

        while(countRobot > 0){
            rotation();
            moveRobot();

        }


    }

    public static int rotation(){
        Kan toUp = down.poll();
        Kan toDown = up.pollLast();
        up.offerFirst(toUp);
        down.offerLast(toDown);
        checkDown();
        return 1;
    }

    public static void checkDown(){
        // 내리는 위치 확인
        Kan lastUp = up.peekLast();
        if(lastUp.isRobot){
            lastUp.isRobot = false;
            countRobot--;
        }
    }

    public static int moveRobot(){
        Object[] upArray = up.toArray();
        for(int i=up.size()-2; i>=0; i--){
            if(((Kan)upArray[i]).isRobot && !((Kan)upArray[i+1]).isRobot){
                ((Kan)(upArray[i])).isRobot = false;
                ((Kan)(upArray[i])).isRobot = true;
            }
        }
        checkDown();
        return 2;
    }
}

class Kan{
    int hp=0;
    boolean isRobot=false;
    Kan(int hp){this.hp = hp;}
}