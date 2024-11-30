#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

const int INF = INT_MAX; // 무한대 정의

void floydWarshall(vector<vector<int>>& dist, int n) {
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
}

pair<int, int> findFurthestNodes(const vector<vector<int>>& dist, int n) {
    int maxDistance = -1;
    pair<int, int> result = {INF, INF};

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (i != j && dist[i][j] != INF && dist[i][j] > maxDistance) {
                maxDistance = dist[i][j];
                result = {i, j};
            } else if (i != j && dist[i][j] == maxDistance) {
                if (i < result.first || (i == result.first && j < result.second)) {
                    result = {i, j};
                }
            }
        }
    }

    return result;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));

    for (int i = 1; i <= n; ++i) {
        dist[i][i] = 0; // 자기 자신으로 가는 경로의 길이는 0
    }

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w); // 간선 가중치 저장 (최소값 유지)
    }

    floydWarshall(dist, n);

    pair<int, int> result = findFurthestNodes(dist, n);
    cout << result.first << " " << result.second << endl;

    return 0;
}