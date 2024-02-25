import java.util.*;
import java.io.*;
public class S8979_올림픽 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        PriorityQueue<Country> que = new PriorityQueue<>();

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            st.nextToken();
            Country country = new Country(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            que.offer(country);
        }

    }
}

class Country implements Comparable<Country>{
    int gold=0, silver=0, bronze=0;

    Country(int gold, int silver, int bronze){
        this.gold = gold; this.silver = silver; this.bronze = bronze;
    }

    @Override
    public int compareTo(Country o) {
        if(this.gold > o.gold){
            return 1;
        } else if(this.gold == o.gold){
            if(this.silver > o.silver){
                return 1;
            } else if(this.silver == o.silver){
                if(this.bronze > o.bronze){
                    return 1;
                } else if(this.bronze == o.bronze){
                    return 0;
                }
            }
        }
        return -1;
    }
}