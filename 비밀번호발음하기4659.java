import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 비밀번호발음하기4659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        Set<Character> vowel = new HashSet<>();
        vowel.add('a'); vowel.add('e'); vowel.add('o'); vowel.add('u'); vowel.add('i');
        String input;
        StringBuilder sb=new StringBuilder();
        while(!"end".equals(input= br.readLine())){
            int n=input.length();
            char prev=input.charAt(0);
            int cnt=1;
            boolean isValid=true, hasVowel=vowel.contains(prev);
            for(int i=1;i<n;i++){
                char cur=input.charAt(i);
                if(vowel.contains(cur) && vowel.contains(prev)){
                    hasVowel=true;
                    if(cur==prev){
                        if(cur!='e' && cur!='o') {
                            isValid=false;
                            break;
                        }
                    }
                    if(++cnt==3){
                        isValid=false;
                        break;
                    }
                }
                else if(!vowel.contains(cur) && !vowel.contains(prev)){
                    if(cur==prev){
                        isValid=false;
                        break;
                    }
                    if(++cnt==3){
                        isValid=false;
                        break;
                    }
                }
                else{
                    cnt=1;
                    hasVowel=true;
                }
                prev=cur;
            }

            sb.append("<").append(input).append("> is ");
            if(!isValid || !hasVowel){
                sb.append("not ");
            }
            sb.append("acceptable.\n");
        }
        System.out.print(sb.toString());
    }
}
