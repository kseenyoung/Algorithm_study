import java.io.*;

public class 단어공부1157 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String word=br.readLine();

        int[] alpha=new int[26];

        for(char c: word.toCharArray()){
            int k=c-'a';
            if(k<0){
                k=c-'A';
            }
            if(k<26){
                alpha[k]++;
            }
        }
        int mi=0, num=1;
        for(int i=1;i<26;i++){
            if(alpha[i]>alpha[mi]){
                mi=i;
                num=1;
            } else if(alpha[i]==alpha[mi]){
                num++;
            }
        }

        if(num>1){
            System.out.println("?");
        }else {
            System.out.println((char)('A'+mi));
        }
    }
}
