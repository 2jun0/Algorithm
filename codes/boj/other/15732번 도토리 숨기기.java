import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        long D = Integer.parseInt(st.nextToken());

        List<Rule> rules = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            rules.add(new Rule(A, B, C));
        }

        System.out.println(findBoxNumber(N, rules, D));
    }

    private static int findBoxNumber(int N, List<Rule> rules, long D) {
        int start = 0;
        int end = N;

        // 위로 갈수록 상자 번호별 누적 도토리 수가 커진다
        while (start < end) {
            int mid = (start + end) / 2;
            long midCumulateCount = sumOfCumulateCountOf(mid, rules);

            if (D <= midCumulateCount) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return end;
    }

    private static long sumOfCumulateCountOf(int boxNumber, List<Rule> rules) {
        return rules.stream()
            .mapToLong(rule -> rule.cumulateCountOf(boxNumber))
            .sum();
    }

    static class Rule {
        private final int A;
        private final int B;
        private final int C;

        Rule(int A, int B, int C) {
            this.A = A;
            this.B = B;
            this.C = C;
        }

        long cumulateCountOf(int x) {
            if (x < A) return 0;
            if (x >= B) return (B - A) / C + 1;

            return (x - A) / C + 1;
        }
    }
}