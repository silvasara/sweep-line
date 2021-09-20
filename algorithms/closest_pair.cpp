/* 
Adaptação do código de Edson Alves, disponível em:
https://github.com/edsomjr/TEP/blob/master/Geometria_Computacional/slides/SL-2/closest.cpp
*/ 

#include <bits/stdc++.h>

using namespace std;
using point = pair<int, int>;

#define x first
#define y second

double get_distance(const point& P, const point& Q){
    return hypot(P.x - Q.x, P.y - Q.y);
}

pair<point, point> get_closest_pair(vector<point>& ps){
    size_t N = ps.size();
    sort(ps.begin(), ps.end());

    // Assume que N > 1
    auto distance = get_distance(ps[0], ps[1]);
    auto closest = make_pair(ps[0], ps[1]);

    set<point> S;
    S.insert(point(ps[0].y, ps[0].x));
    S.insert(point(ps[1].y, ps[1].x));

    for (int i = 2; i < N; ++i){
        auto P = ps[i];
        auto it = S.lower_bound(point(P.y - distance, 0));

        while (it != S.end()){
            auto Q = point(it->second, it->first);

            if (Q.x < P.x - distance){
                it = S.erase(it);
                continue;
            }

            if (Q.y > P.y + distance)
                break;

            auto curr_distance = get_distance(P, Q);

            if (curr_distance < distance){
                distance = curr_distance;
                closest = make_pair(P, Q);
            }

            ++it;
        }

        S.insert(point(P.y, P.x));
    }

    return closest;
}

int main(){
    vector<point> P {
        {2, 4},
        {5, 3},
        {8, 1},
        {3, 6},
        {1, 1},
        {4, 4},
        {8, 5},
        {6, 2},
        {1, 6},
        {7, 4},
        {8, 6},
        {3, 2},
        {6, 5},
        {-1, 4}
    };

    auto closest_pair = get_closest_pair(P);

    printf("A: (%d, %d), B: (%d, %d)\n",
           closest_pair.first.first, closest_pair.first.second,
           closest_pair.second.first, closest_pair.second.second
    );

    return 0;
}
