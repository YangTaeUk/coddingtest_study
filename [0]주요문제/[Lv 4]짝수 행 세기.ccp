/**
 * 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68647
 * 알고리즘: DP (동적 계획법)
 * 시간 복잡도: O(N^2 * M)  // N = 행의 개수, M = 열의 개수
 *
 * 최종 결과는 MOD = 10^7 + 19 로 나눈 나머지를 반환합니다.
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// MOD 값 설정: 모든 계산은 이 값으로 나눈 나머지를 사용
long long MOD = 1e7 + 19;

// 조합 (nCr) 값을 저장할 2차원 벡터, 메모이제이션 용도
vector<vector<long long>> combi;

/**
 * getCombination: n개 중 r개를 선택하는 조합의 수를 MOD로 나눈 값을 구하는 함수
 *
 * @param n : 전체 원소의 개수
 * @param r : 선택할 원소의 개수
 * @return nCr (MOD MOD) 값
 */
long long getCombination(int n, int r) {
    // 선택하는 개수가 전체보다 많으면 0 반환
    if (n < r) return 0;

    // 이미 계산한 값이면 바로 반환 (메모이제이션)
    long long& ret = combi[n][r];
    if (ret != -1) return ret;

    // n과 r이 같거나 r이 0이면 경우의 수는 1 (기저 사례)
    if (n == r || r == 0) return ret = 1;

    // 점화식: C(n, r) = C(n-1, r-1) + C(n-1, r)
    return ret = (getCombination(n - 1, r - 1) + getCombination(n - 1, r)) % MOD;
}

/**
 * solution: 주어진 arr 행렬에 대해, 각 열의 1의 개수를 유지하면서
 *           최종적으로 각 행의 1의 개수가 짝수가 되는 경우의 수를 구하는 함수.
 *
 * @param arr : 입력 0-1 행렬 (벡터 형태)
 * @return 조건을 만족하는 행렬의 경우의 수 (MOD로 나눈 나머지)
 */
int solution(vector<vector<int>> arr) {
    // 행렬의 행 개수 n과 열 개수 m
    int n = (int)arr.size();
    int m = (int)arr[0].size();

    // 조합 값을 저장할 벡터 초기화 (문제 조건 최대 크기 300 고려)
    combi = vector<vector<long long>>(301, vector<long long>(301, -1));

    // oneCnts[j] : 입력 행렬에서 j번째 열(1-indexed)의 1의 개수를 저장
    // 인덱스를 1부터 사용하기 위해 m+1 크기로 선언
    vector<int> oneCnts(m+1, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // 열 번호를 1부터 시작하도록 j+1에 누적
            oneCnts[j+1] += arr[i][j];
        }
    }

    /**
     * dp[column][num] 정의:
     *   - column: 현재까지 처리한 열의 개수 (1-indexed로 사용, 1~m)
     *   - num: 현재까지 처리한 열들에서, 1의 개수가 짝수인 행의 개수
     *
     * dp[column][num]의 값은,
     *   arr[0~n][0~column]까지 고려했을 때, num개의 행이 "1의 개수가 짝수"인 경우의 수를 의미합니다.
     */
    vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));

    // 첫 번째 열 처리:
    // 첫 번째 열에서 1의 개수가 oneCnts[1]개이므로, 전체 n행 중
    // 1이 채워지지 않은 행(즉, 짝수(0)를 가진 행)의 수는 n - oneCnts[1]개가 됨.
    // 그리고 첫 번째 열의 경우의 수는 n행 중 oneCnts[1]개를 선택하는 조합 수.
    dp[1][n - oneCnts[1]] = getCombination(n, oneCnts[1]);

    // 2번째 열부터 m번째 열까지 차례대로 처리
    for (int column = 1; column <= m; column++) {
        // 현재 열에서 1의 개수 (문제에서 정해진 값)
        int oneCnt = oneCnts[column];

        // 현재까지 처리한 열들에서 짝수 상태의 행의 개수(num)를 고려
        for (int num = 0; num <= n; num++) {
            // 현재 상태에서 dp[column-1][num]에 해당하는 경우가 없다면 넘어감
            // (암시적으로 0인 경우, 아래 루프에서는 아무 것도 더해지지 않음)

            // 현재 열에서 1을 넣을 때, 기존 짝수 행 중 몇 개에 1을 넣을 것인지 결정
            // k: 기존 짝수 행 중 1을 추가하여 홀수로 바뀌게 될 행의 개수
            for (int k = 0; k <= oneCnt; k++) {
                // 현재 열에서 1의 총 개수 oneCnt 중에서,
                // k개를 기존 짝수 행에 넣으면, 나머지 oneCnt - k 개는 기존 홀수 행에 넣어야 함.
                int willSetOddRow = oneCnt - k;

                // 전환 후, 1을 추가한 후 짝수가 되는 행의 개수를 계산:
                //   - 기존 짝수 행에서 1을 넣지 않은 행: (num - k)
                //   - 기존 홀수 행에서 1을 넣어 짝수로 전환된 행: willSetOddRow
                int willBeEvenRowCnt = (num - k) + willSetOddRow;

                // 만약 계산 결과가 불가능한 경우(음수가 되거나 전체 행 수를 초과)에는 continue
                if (willSetOddRow < 0 || willBeEvenRowCnt > n || willBeEvenRowCnt < 0)
                    continue; // 해당 경우는 성립할 수 없으므로 건너뜁니다.

                // 경우의 수 계산:
                //   - 기존 짝수 행 중 k개에 1을 넣는 경우의 수: getCombination(num, k)
                //   - 기존 홀수 행 중 (oneCnt - k)개에 1을 넣어 짝수로 전환하는 경우의 수:
                //         getCombination(n - num, oneCnt - k)
                // 두 경우의 수를 곱하면, 현재 열에서 이 배분으로 인해 전환될 경우의 수가 됨.
                long long numOfCase = (getCombination(num, k) * getCombination(n - num, oneCnt - k)) % MOD;

                // dp 테이블 업데이트:
                // 이전 열까지의 경우의 수(dp[column-1][num])에 현재 열의 경우의 수(numOfCase)를 곱하여,
                // 현재 열 처리 후 짝수 행의 개수가 willBeEvenRowCnt인 경우의 수를 누적.
                dp[column][willBeEvenRowCnt] += dp[column-1][num] * numOfCase % MOD;
                dp[column][willBeEvenRowCnt] %= MOD;
            }
        }
    }

    // 마지막 열(m번째 열)까지 처리한 후, 모든 행이 짝수가 되어야 하므로 dp[m][n]이 정답.
    return dp[m][n];
}
