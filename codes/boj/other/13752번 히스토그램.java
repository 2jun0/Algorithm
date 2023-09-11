import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        final int N = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < N; i++) {
            final int k = Integer.parseInt(br.readLine().trim());
            System.out.println("=".repeat(k));
        }
    }
}
