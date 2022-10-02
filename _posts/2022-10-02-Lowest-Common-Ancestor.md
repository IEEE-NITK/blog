---
 layout: post
 title: "Lowest Common Ancestor"
 author_github: sathuhebbar
 date: 2022-10-02 00:00:00
 image: '/assets/img/'
 description: 'A few LCA finding algorithms'
 tags:
 - trees
 categories:
 - CompSoc
 github_username: sathuhebbar
 use_math: true
---

$T(V, E)$ is a tree on $n$ vertices rooted at vertex $r$. <br>
Suppose $u, v$ belong to V. <br>
Consider the list of all vertices on the path from $u$ to the root written in order: <br>
$P(u)$ = $[u$, $u$<sub>$1$</sub>, $u$<sub>$2$</sub>, ... $r]$ <br>
Similarly for v:
$P(v)$ = $[v$, $v$<sub>$1$</sub>, $v$<sub>$2$</sub>, ... $r]$ <br>
Note that $len(P(u)) = 1 + depth(u) $. <br>
The first vertex common to the two lists $P(u)$ and $P(v)$ is $LCA(u, v)$.

# Algorithm 1:
The naive algorithm:
The first vertex common to $P(u)$ and $P(v)$ is the last vertex common to $reversed(P(u))$ and $reversed(P(v))$.
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
The height $h$ is the largest depth of any vertex in the tree. <br>
An LCA query with this algorithm performs $O(max(len(P(u)), len(P(v))))$ operations, <br>
which is, in the worst case $O(h)$.

# Algorithm 2
Here is an $O((log(h))$<sup>$2$</sup>$)$ solution. <br>
We preprocess the tree in $O(n log(n))$ time to make a table that can find the ancestor $k$ levels
above the specified node in $O(log(h))$. <br>
1. Perform a DFS traversal and keep track of all ancestors of a node using a list. <br>
2. Store ancestors which are $x$ levels above each node where $x$ is a power of two. <br>
3. To answer the query $kabove$, jump to the farthest known ancestor that is not more than k levels above the specified node. <br>
4. Call $kabove$ on that node with a reduced $k$. <br>

With $kabove$, we can binary search for the LCA. 
1. Let $l = 0$ and $r = min(depth(u), depth(v))$. The depth of lca(u, v) lies in $[l, r]$.
2. If the ancestors at depth $m$ match, $lca(u, v)$ is at a depth $>= m$ .
   Otherwise, it is at a depth lower than $m$.
<br>
This, and the code for later algorithms are written as solutions to the 'Company Queries II' problems on the CSES site.
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
$O(n log(n))$ preprocessing, $O((log(h))$<sup>$2$</sup>$)$ per query.

# Algorithm 3
If we assign a value to each vertex $val[v]$ during a DFS traversal
such that the child chosen is assigned the smallest untaken value after $val[v]$,
it is easy to see that all children of $v$ will have values in the range
$[val[v] + 1, val[v] + nd[v] - 1]$ where $nd[v] = 1 +$ number of descendants of $v$.
Thus, testing whether $v$ is an ancestor of $u$ is just checking if
$val[u]$ lies in the above range.

With this addition, the below improves on the earlier algorithm. <br>
1. If u is an ancestor of v or v is an ancestor of u or u is v, we are done.
2. Otherwise, look for the farthest among the known ancestors of $v$ which is not an ancestor of $u$. If there is no such node, the parent of v is $lca(u, v)$.
3. If there is such a node $x$, the required LCA is $lca(x, u)$. 
<br>

```cpp
#include <bits/stdc++.h>

using namespace std;

void init_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
}

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

# Algorithm 4
The offline version of algorithm 3 can find LCAs in $O(log(n))$. 
<h3>Storing the queries:</h3>
1. Keep a list of lists $qs$ of length $n + 1$ and two lists $vs, ans$ of length $q$. 
2. For every query $(u, v)$, append the query number $j$ to $qs[u]$ and let $vs[j] = v$. <br>
<h3>Algorithm:</h3>
1. We find $lca(u, v)$ during another DFS traversal. 
2. When $u$ is reached, we have $P(u)$.
<br>
For every $j$ in $qs[u]$, let $v = vs[j]$,   
3. If $u$ is an ancestor of $v$, we are done.
4. Otherwise, binary search for $lca(u, v)$ in $P(u)$ using the ancestor test.
5. Assign the value to $ans[j]$.
<br>

```cpp
#include <bits/stdc++.h>

using namespace std;

void init_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
}

vector<int> vs, ans, nd, val, P;
vector<vector<int>> adj, qs;

int dfs1(int u, int vl) {
    nd[u] = 1, val[u] = vl;
    for (int x : adj[u]) {
        vl = dfs1(x, vl + 1);
        nd[u] += nd[x];
    }
    return vl;
}

int is_ancestor(int u, int v) {
    return val[v] >= val[u] and val[v] < val[u] + nd[u];
}

void dfs2(int u, vector<int> &P) {
    for (int j : qs[u]) {
        int v = vs[j];
        if (is_ancestor(u, v))
            ans[j] = u;
        else {
			int l = 0, r = P.size() - 1;
            while (r - l > 2) {
                int m = l + (r - l) / 2;
                if (is_ancestor(P[m], v))
                    l = m;
                else
                    r = m - 1;
            }
            for (int m = r; m >= l; m--)
                if (is_ancestor(P[m], v)) {
                    ans[j] = P[m];
                    break;
                }
        }
    }
    P.push_back(u);
    for (int x : adj[u])
        dfs2(x, P);
    P.pop_back();
}

int main() {
    init_io();
    int n, q;
    cin >> n >> q;
    adj.resize(n + 1);
    qs.resize(n + 1);
    ans.resize(q);
    vs.resize(q);
    val.resize(n + 1);
    nd.resize(n + 1);
    for (int j = 2; j <= n; j++) {	
        int x;
        cin >> x;
        adj[x].push_back(j);
    }
    dfs1(1, 0);
    for (int j = 0; j < q; j++) {
        int u, v;
        cin >> u >> v;
        qs[u].push_back(j);
        vs[j] = v;
    }
    dfs2(1, P);
    for (int j = 0; j < q; j++)
        cout << ans[j] << '\n';
    return 0;
}
```
# Resources:
Here are a few interesting sites:
1. LCA and RMQ, [CP-Algorithms](https://cp-algorithms.com/graph/lca.html)
2. Farach Colton and Bender, $O(n)$ or $O(n log(n))$ preprocessing, $O(1)$ query
[CP-Algorithms](https://cp-algorithms.com/graph/lca_farachcoltonbender.html)
3. Tarjan's algorithm (offline), 
[CP-Algorithms](https://cp-algorithms.com/graph/lca_tarjan.html)
4. [USACO -- Binary Jumping](https://usaco.guide/plat/binary-jump?lang=cpp)
5. CSES tree algorithms section