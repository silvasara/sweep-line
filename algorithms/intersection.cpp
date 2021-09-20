/* 
Adaptação do código de Edson Alves, disponível em:
https://github.com/edsomjr/TEP/blob/master/Geometria_Computacional/slides/SL-1/points.cpp
*/ 

#include <bits/stdc++.h>

using namespace std;

class BITree {
private:
    vector<int> trees;
    size_t N;

    int get_LSB(int n){
        return n & (-n);
    }

public:
    BITree(size_t n) : trees(n + 1, 0), N(n) {}

    int get_RSQ(int i){
        int sum = 0;

        while (i >= 1){
            sum += trees[i];
            i -= get_LSB(i);
        }

        return sum;
    }

    void add(size_t i, int x){
        if (i == 0)
            return;

        while (i <= N){
            trees[i] += x;
            i += get_LSB(i);
        }
    }
};

struct Point {
    int x, y;
};

struct Interval {
    Point A, B;
};

int get_index(const vector<int>& hs, int value){
    auto it = lower_bound(hs.begin(), hs.end(), value);

    return it - hs.begin() + 1;     // Contagem inicia em 1
}

int count_intersections(const vector<Interval>& intervals){
    struct Event {
        int type, x;
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
    set<int> ys;        // Conjunto para compressão das coordenadas

    for (size_t i = 0; i < intervals.size(); ++i){
        auto I = intervals[i];

        ys.insert(I.A.y);
        ys.insert(I.B.y);

        auto xmin = min(I.A.x, I.B.x);
        auto xmax = max(I.A.x, I.B.x);

        if (I.A.x == I.B.x)     // Vertical
            events.push_back( { 2, xmin, i });
        else{                    // Horizontal
            events.push_back( { 1, xmin, i });
            events.push_back( { 3, xmax, i });
        }
    }

    sort(events.begin(), events.end());
    
    vector<int> hs(ys.begin(), ys.end());   // Mapa de compressão
    BITree fenwick(hs.size());
    auto total = 0;

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
    vector<Interval> intervals { 
        {Point{2, 6}, Point{5, 6}},
        {Point{1, 5}, Point{6, 5}},
        {Point{5, 4}, Point{8, 4}},
        {Point{3, 3}, Point{7, 3}},
        {Point{5, 2}, Point{8, 2}},
        {Point{1, 1}, Point{4, 1}},
        {Point{4, 7}, Point{4, 2}},
        {Point{2, 3}, Point{2, 0}},
        {Point{6, 3}, Point{6, 1}},
    };

    auto ans = count_intersections(intervals);

    cout << ans << '\n';

    return 0;
}
