/* 
Adaptação do código de Edson Alves, disponível em:
https://github.com/edsomjr/TEP/blob/master/Geometria_Computacional/slides/SL-1/points.cpp
*/ 

#include <bits/stdc++.h>

using namespace std;
using ll = long long int;

class BITree {
private:
    vector<ll> trees;
    size_t N;

    ll get_LSB(ll n){
        return n & (-n);
    }

public:
    BITree(size_t n) : trees(n + 1, 0), N(n) {}

    ll get_RSQ(ll i){
        ll sum = 0;

        while (i >= 1){
            sum += trees[i];
            i -= get_LSB(i);
        }

        return sum;
    }

    void add(size_t i, ll x){
        if (i == 0)
            return;

        while (i <= N){
            trees[i] += x;
            i += get_LSB(i);
        }
    }
};

struct Point{
    ll x, y;
};

struct Interval{
    Point A, B;
};

ll get_index(const vector<ll>& hs, ll value){
    auto it = lower_bound(hs.begin(), hs.end(), value);

    return it - hs.begin() + 1;     // Contagem inicia em 1
}

ll count_intersections(const vector<Interval>& intervals){
    struct Event {
        ll type, x;
        size_t idx;

        bool operator<(const Event& e) const{
            if (x != e.x)
                return x < e.x;

            if (type != e.type)
                return type < e.type;

            return idx < e.idx;
        }
    };

    vector<Event> events;
    set<ll> ys;        // Conjunto para compressão das coordenadas

    for (size_t i = 0; i < intervals.size(); ++i){
        auto I = intervals[i];

        ys.insert(I.A.y);
        ys.insert(I.B.y);

        auto xmin = min(I.A.x, I.B.x);
        auto xmax = max(I.A.x, I.B.x);

        if (I.A.x == I.B.x)     // Vertical
            events.push_back({2, xmin, i });
        else{                  // Horizontal
            events.push_back({1, xmin, i });
            events.push_back({3, xmax, i });
        }
    }

    sort(events.begin(), events.end());
    
    vector<ll> hs(ys.begin(), ys.end());   // Mapa de compressão
    BITree fenwick(hs.size());
    ll total = 0;

    for (const auto& event : events){
        auto I = intervals[event.idx];

        switch (event.type) {
            case 1: {
                auto y = get_index(hs, I.A.y);
                fenwick.add(y, 1);
            }
                break;

            case 2: {
                auto ymin = min(get_index(hs, I.A.y), get_index(hs, I.B.y));
                auto ymax = max(get_index(hs, I.A.y), get_index(hs, I.B.y));
                total += fenwick.get_RSQ(ymax) - fenwick.get_RSQ(ymin - 1);
            }
                break;

            default: {
                auto y = get_index(hs, I.B.y);
                fenwick.add(y, -1);
            }
        }
    }

    return total;
}

int main(){
    vector<Interval> intervals;

    ll x_a, y_a;
    ll x_b, y_b;

    while(cin >> x_a >> y_a >> x_b >> y_b){
        Point A = {x_a, y_a};
        Point B = {x_b, y_b};

        intervals.push_back({A, B});
    }

    auto ans = count_intersections(intervals);

    cout << ans << '\n';

    return 0;
}
