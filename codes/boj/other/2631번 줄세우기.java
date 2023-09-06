import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        final int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        for(int i = 0; i < N; i ++ ){
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[] maxLcsLenByLast = new int[N+1];

        for (int i = 0; i < N; i++) {
            maxLcsLenByLast[arr[i]] = 1;
            for (int x = arr[i] - 1; x > 0; x--) {
                maxLcsLenByLast[arr[i]] = Math.max(maxLcsLenByLast[arr[i]], maxLcsLenByLast[x] + 1);
            }
        }

        final int lcsLen = Arrays.stream(maxLcsLenByLast).max().getAsInt();

        System.out.println(N - lcsLen);
    }    
}
