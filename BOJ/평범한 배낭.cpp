#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int n, maxW;
int dp[101][100001];
vector<pair<int, int>> item; //weight-value

int ks(int i, int w) { //knapsack algorithm

	if (i == n) return 0;
	if (dp[i][w] > 0) return dp[i][w];

	int v1 = 0;
	if (w + item[i].first <= maxW) //if available
		v1 = item[i].second + ks(i + 1, w + item[i].first); //include i
	int v2 = ks(i + 1, w); //not include i

	dp[i][w] = max(v1, v2);

	return dp[i][w];
}

int main() {

	cin >> n >> maxW; //number of items, max weight

	for (int i = 0; i < n; i++) { //get input
		int w, v;
		cin >> w >> v;
		item.push_back(make_pair(w, v));
	}

	cout << ks(0, 0);

	return 0;
}