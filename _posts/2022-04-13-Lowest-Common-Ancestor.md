---
 layout: post
 title: "Lowest Common Ancestor"
 author_github: sathuhebbar
 date: 2022-04-13 23:32:44
 image: '/assets/img/'
 description: 'A few LCA finding algorithms'
 tags:
 - trees
 categories:
 - CompSoc
 github_username: sathuhebbar
---

<b>T (V, E)</b> is a tree on <b>n</b> vertices rooted at vertex <b>r</b>. <br>
Suppose <b>u, v</b> belong to V. <br>
Consider the list of all vertices on the path from u to the root written in order:
<b>P(u)</b> = [u, u<sub>1</sub>, u<sub>2</sub>, ... r] <br>
Similarly for v:
<b>P(v)</b> = [v, v<sub>1</sub>, v<sub>2</sub>, ... r] <br>
Note that <b>len(P(u)) = 1 + depth(u) </b>. <br>
The first vertex common to the two lists P(u) and P(v) is <b>LCA(u, v)</b>.

<h2>Algorithm 1:</h2>
The naive algorithm:
The first vertex common to P(u) and P(v) is the last vertex common to <b>reversed(P(u))</b> and <b>reversed(P(v))</b>.
```
def P(u, p):
    ls, x = [], u
    while x != 1:
        ls.append(x)
        x = p[x - 2]
    ls.append(1)
    return ls

def lca(u, v, p):
    a, b = P(u, p), P(v, p)
    for j in range(min(len(a), len(b))):
        if a[len(a) - 1 - j] != b[len(b) - 1 - j]:
            return a[len(a) - 1 - j]
    return (u if len(a) < len(b) else v)

# Driver code -- Assume a tree rooted at vertex 1
# p is the list of parent vertices
n = int(input())
p = [int(x) for x in input().split()]
u, v = map(int, input().split())
print(lca(u, v, p))
```
<b> Time complexity </b> <br>
The height <b>h</b> is the largest depth of any vertex in the tree. <br>
An LCA query with this algorithm performs <b>O(max(len(P(u)), len(P(v))))</b> operations, <br>
which is, in the worst case <b>O(h)</b>.

<h2>Algorithm 2</h2>
Here is an <b>O((log h)<sup>2</sup>)</b> solution. <br>
We preprocess the tree in <b>O(n log(n))</b> time to make a table that can find the ancestor k levels
above the specified node in <b>O(log h)</b>. <br>
1. Perform a DFS traversal and keep track of all ancestors of a node using a list. <br>
2. Store ancestors which are x levels above each node where x is a power of two. <br>
3. To answer the query <b>kabove</b>, jump to the farthest known ancestor that is not more than k levels above the specified node. <br>
4. Call <b>kabove</b> on that node with a reduced k. <br>

With <b>kabove</b>, we can binary search for the LCA. 
Let <b>l = 0</b> and <b>r = min(depth(u), depth(v))</b>. The depth of lca(u, v) lies in <b>[l, r]</b>.
If the ancestors at depth <b>m</b> match, <b>lca(u, v)</b>
is at that depth or is below. Otherwise, it is above.
Try submitting this code for the 'Company Queries' problem on CSES.
``` python 
class Engine:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.adj = [[] for _ in range(n + 1)]
        for j in range(2, n + 1):
            self.adj[p[j - 2]].append(j)
        self.ls = [0] * (n + 1)
        self.logs()
        self.mat = [[-1] * (self.log(n) + 1) for _ in range(n + 1)] 
        self.depth = [0] * (n + 1)
        self.dfs(1, [], 0)
    def log(self, u):
        #print(self.ls)
        return self.ls[u]
    def logs(self):
        v, lg = 1, 0
        for j in range(2, self.n + 1):
            if j >= 2 * v:
                lg += 1
                v *= 2
            self.ls[j] = lg
    def dfs(self, v, P, d):
        x = 1
        #print(v, P, d)
        self.depth[v] = d
        while x <= d:
            self.mat[v][self.log(x)] = P[-x] 
            x *= 2
        P.append(v)
        for x in self.adj[v]:
            self.dfs(x, P, d + 1)
        P.pop()
    def kabove(self, v, k):
        if k == 0:
            return v
        elif self.depth[v] < k:
            return -1
        else:
            x = self.log(k)
            return self.kabove(self.mat[v][x], k - (1 << x))
    def lca(self, u, v):
        if u == v:
            return u
        l, r = 0, min(self.depth[u], self.depth[v])
        while r - l > 2:
            m = l + (r - l) // 2
            x, y = self.kabove(u, self.depth[u] - m), self.kabove(v, self.depth[v] - m)
            if x == y:
                l = m
            else:
                r = m - 1
        for m in range(r, l - 1, -1):
            x, y = self.kabove(u, self.depth[u] - m), self.kabove(v, self.depth[v] - m)
            if x == y:
                return x
# Driver code -- Assume a tree rooted at 1, we answer q queries
n, q = map(int, input().split())
p = [int(x) for x in input().split()]
e = Engine(n, p)
for _ in range(q):
    u, v = map(int, input().split())
    print(e.lca(u, v))
``` 
<b> Time complexity </b> <br>
<b>O(n log(n))</b> preprocessing, <b>O((log h)<sup>2</sup>)</b> per query.

<h2>Algorithm 3</h2>
If we assign a value to each vertex <b>val[v]</b> during a DFS traversal
such that the child chosen is assigned the smallest untaken value after <b>val[v]</b>,
it is easy to see that all children of <b>v</b> will have values in the range
<b>[val[v] + 1, val[v] + nd[v] - 1]</b> where <b>nd[v] = 1 + number of descendants of v</b>.
Thus, testing whether <b>v</b> is an ancestor of <b>u</b> is just checking if
<b>val[u]</b> lies in the above range.

With this addition, the below improves on the earlier algorithm. <br>
1. If u is an ancestor of v or v is an ancestor of u or u is v, we are done.
2. Otherwise, look for the farthest among the known ancestors of <b>v</b> which is not an ancestor of <b>u</b>. If there is no such node, the parent of v is <b>lca(u, v)</b>.
3. If there is such a node <b>x</b>, the required LCA is <b>lca(x, u)</b>. 
<br>

```cpp
#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;
using vll = vector<ll>;
using vld = vector<ld>;
using vvi = vector<vector<int>>;

string to_string(bool b) { return b ? "true" : "false"; }

string to_string(string s) { return s; }

template <typename T, typename U> string to_string(pair<T, U> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <typename T, typename U, typename V>
string to_string(tuple<T, U, V> trip) {
    return "(" + to_string(get<0>(trip)) + ", " + to_string(get<1>(trip)) +
           ", " + to_string(get<2>(trip)) + ")";
}

template <typename T> string to_string(const T &c) {
    string out = "{";
    bool f = true;
    for (const auto &x : c) {
        if (f) {
            out += to_string(x);
            f = false;
            continue;
        }
        out += ", " + to_string(x);
    }
    out += "}";
    return out;
}

template <typename T> void print(const T &x) { cout << to_string(x) << '\n'; }

void init_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
}

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vector<int>>;

struct Engine {
    vector<int> lgt, dpth, nd, val;
    vector<vector<int>> adj, table;
    int n;
    Engine(int n, vector<int> &p) {
        this->n = n;
        lgt.resize(n + 1);
        adj.resize(n + 1);
        dpth.resize(n + 1);
        nd.resize(n + 1);
        val.resize(n + 1);
        for (int j = 2; j <= n; j++)
            adj[p[j - 2]].push_back(j);
        gen_logs();
        table = vector<vector<int>>(n + 1, vector<int>(lgt[n] + 1, -1));
        vector<int> anc;
        process(1, 0, 0, anc);
    }

    int process(int v, int d, int vl, vector<int> &anc) {
        val[v] = vl;
        dpth[v] = d;
        int x = 1;
        while (x <= d) {
            table[v][lgt[x]] = anc[d - x];
            x *= 2;
        }
        anc.push_back(v);
        nd[v] = 1;
        for (int x : adj[v]) {
            vl = process(x, d + 1, vl + 1, anc);
            nd[v] += nd[x];
        }
        anc.pop_back();
        return vl;
    }

    int is_ancestor(int u, int v) {
        return val[v] >= val[u] and val[v] < val[u] + nd[u];
    }

    int lca(int u, int v) { 
        if (u == v)
            return u;
        if (is_ancestor(u, v))
            return u;
        if (is_ancestor(v, u))
            return v;
        int l = 0, r = lgt[dpth[v]];
        while (r - l > 2) {
            int m = l + (r - l) / 2;
            int x = table[v][m];
            if (is_ancestor(x, u))
                r = m;
            else
                l = m + 1;
        }
        if (l == 0 and is_ancestor(table[v][l], u))
            return table[v][l];
        for (int j = l; j <= r; j++)
            if (j > 0 and is_ancestor(table[v][j], u))
                return lca(table[v][j - 1], u);
        return lca(table[v][r], u);
    }

    void gen_logs() {
        int v = 1, lg = 0;
        for (int j = 1; j <= n; j++) {
            if (j == 2 * v)
                lg++, v *= 2;
            lgt[j] = lg;
        }
    }
};

// Driver code -- Assume a tree rooted at 1, we answer q queries
signed main() {
    init_io();
    int n, q;
    cin >> n >> q;
    vector<int> p(n + 1);
    for (int j = 2; j <= n; j++)
        cin >> p[j - 2];
    Engine e(n, p);
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << e.lca(u, v) << '\n';
    }
    return 0;
}
```
These are a few elementary algorithms. Here are a few interesting sites:
1. LCA and RMQ, [CP-Algorithms](https://cp-algorithms.com/graph/lca.html) <b></b>
2. Farach Colton and Bender, <b>O(n)</b> or <b>O(n log n)</b> preprocessing, <b>O(1) query</b>
[CP-Algorithms](https://cp-algorithms.com/graph/lca_farachcoltonbender.html)
3. Tarjan's algorithm (offline), 
[CP-Algorithms](https://cp-algorithms.com/graph/lca_tarjan.html)
4. [USACO -- Binary Jumping](https://usaco.guide/plat/binary-jump?lang=cpp)
5. CSES tree algorithms section