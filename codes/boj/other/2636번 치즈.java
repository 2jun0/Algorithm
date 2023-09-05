import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    private static int[] dy = {0, 0, -1, 1};
    private static int[] dx = {-1, 1, 0, 0};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int height = Integer.parseInt(st.nextToken());
        int width = Integer.parseInt(st.nextToken());

        int[][] map = new int[height][width];

        for (int y = 0; y < height; y ++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < width; x ++) {
                map[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        Answer answer = bfs(map);

        System.out.println(answer);

        br.close();
    }

    private static Answer bfs(final int[][] map) {
        final int height = map.length;
        final int width = map[0].length;

        final Deque<Entry> q = new ArrayDeque<Entry>();
        final boolean[][] visited = new boolean[height][width];
        int maxTime = 0;
        int cheeseCntAtMaxTime = 0;

        q.addLast(new Entry(0,0,0));
        visited[0][0] = true;

        while (!q.isEmpty()) {
            final Entry e = q.pollFirst();

            if (maxTime < e.time) {
                maxTime = e.time;
                cheeseCntAtMaxTime = 0;
            }

            if (map[e.y][e.x] == 1 && maxTime == e.time) {
                cheeseCntAtMaxTime ++;
            }

            for (int i = 0; i < 4; i++) {
                final int nxtY = e.y + dy[i];
                final int nxtX = e.x + dx[i];

                if (!rangeOk(nxtY, nxtX, height, width) || visited[nxtY][nxtX]) {
                    continue;
                }

                visited[nxtY][nxtX] = true;
                if (map[nxtY][nxtX] == 1) {
                    q.addLast(new Entry(nxtY, nxtX, e.time + 1));
                } else {
                    q.addFirst(new Entry(nxtY, nxtX, e.time));
                }
            }
        }

        return new Answer(maxTime, cheeseCntAtMaxTime);
    }

    private static boolean rangeOk(final int y, final int x, final int height, final int width) {
        return (0 <= y && y < height) && (0<=x && x<width);
    }

    static class Entry {
        final int y;
        final int x;
        final int time;

        Entry(final int y, final int x, final int time) {
            this.y = y;
            this.x = x;
            this.time =time;
        }
    }

    static class Answer {
        final int maxTime;
        final int cheeseCntAtMaxTime;

        Answer(final int maxTime, final int cheeseCntAtMaxTime) {
            this.maxTime = maxTime;
            this.cheeseCntAtMaxTime = cheeseCntAtMaxTime;
        }

        @Override
        public String toString() {
            return this.maxTime + "\n" + this.cheeseCntAtMaxTime;
        }
    }
}