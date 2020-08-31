

class UF {
  // sz is the size of a group
  int *id, cnt, *sz;

public:
  // Create an empty union find data structure with N isolated sets.
  UF(int N) {
    cnt = N;
    id = new int[N];
    sz = new int[N];
    for (int i = 0; i < N; i++)
      id[i] = i, sz[i] = 1;
  }

  ~UF() {
    delete[] id;
    delete[] sz;
  }

  // Return the id of component corresponding to object p.
  int find(int p) {
    if (p != id[p])
      id[p] = find(id[p]);
    return id[p];
  }

  // Merge to smaller root if greater == false else to larger root. 
  // Should use normal merge as possible as you can. This method cause trouble when 
  // you try to merge (2, 6), and then (6, 3). The larger number 6 should work as a 
  // middleman, however, it's useless if you use this method. 
  // void merge_by_value(int x, int y, bool greater) {
  //   int i = find(x), j = find(y);
  //   id[x] = id[y] = greater ? std::max(i, j) : std::min(i, j);
  // }

  // Replace sets containing x and y with their union.
  void merge(int x, int y) {
    int i = find(x), j = find(y);
    if (i == j)
      return;

    // make smaller root point to larger one
    if (sz[i] < sz[j]) {
      id[i] = j, sz[j] += sz[i];
    } else {
      id[j] = i, sz[i] += sz[j];
    }

    cnt--;
  }

  // Are objects x and y in the same set?
  bool connected(int x, int y) { return find(x) == find(y); }

  // Return the number of disjoint sets.
  int count() { return cnt; }
};