
import java.io.*;
        import java.util.*;

public class S1157_단어공부 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<Character, Integer> map = new HashMap<>();

        String input = br.readLine();
        for(int i=0; i<input.length(); i++){
            char curr = Character.toUpperCase(input.charAt(i));
            map.put(curr, map.getOrDefault(curr, 0)+1);
        }

        char maxChar = 'A';
        int max = map.getOrDefault('A', 0);
        for(int i=66; i<=90; i++){
            char currChar = (char)i;
            int curr = map.getOrDefault(currChar, 0);
            if(curr > max){
                maxChar = (char) i;
                max = curr;
            } else if(curr == max){
                maxChar = '?';
            }
        }

        System.out.print(maxChar);

    }
}