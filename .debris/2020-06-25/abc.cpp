 class UF {
    public:
        vector<int> parent;
        vector<int> rank;
        UF(int n) : parent(n), rank(n, 0) {
            for (int i = 0; i < n; ++i) {
                parent[i] = i;
            }
        }
        int find(int x) {
            if (x != parent[x]) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        void unite(int x, int y) {
            int fx = find(x);
            int fy = find(y);
            if (rank[fx] > rank[fy]) {
                parent[fy] = fx;
            } else {
                parent[fx] = fy;
                if (rank[fx] == rank[fy]) {
                    rank[fy] += 1;
                }
            }
        }
    };