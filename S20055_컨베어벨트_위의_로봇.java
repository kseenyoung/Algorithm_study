import java.io.*;
import java.util.*;
public class S20055_컨베어벨트_위의_로봇 {
    static int countRobot = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N  = Integer.parseInt(st.nextToken());
        int K  = Integer.parseInt(st.nextToken());

        Deque<Kan> up = new ArrayDeque<>();
        Deque<Kan> down = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            Kan kan = new Kan(Integer.parseInt(st.nextToken()));
            if(i < N){
                up.add(kan);
            } else{
                down.add(kan);
            }
        }

        down.peek().isRobot = true;

    }

    public static void rotation(Deque<Kan> up, Deque<Kan> down){
        Kan toUp = down.poll();
        Kan toDown = up.pollLast();
        up.offerFirst(toUp);
        down.offerLast(toDown);
        // 내리는 위치 확인
        Kan lastUp = up.peekLast();
        if(lastUp.isRobot){
            lastUp.isRobot = false;
        }
    }
}

class Kan{
    int hp=0;
    boolean isRobot=false;
    Kan(int hp){this.hp = hp;}
}