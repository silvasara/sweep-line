/* 
Adaptação do código de Edson Alves, disponível em:
https://github.com/edsomjr/TEP/blob/master/Geometria_Computacional/slides/CH-1/andrew.cpp
*/ 

#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using ll = long long int;

template<typename T> struct Point{
    T x, y;

    bool operator<(const Point& P) const{
        return x == P.x ? y < P.y : x < P.x;
    }
};

template<typename T> T get_determinant(const Point<T>& P, const Point<T>& A, const Point<T>& B){
    return (P.x * A.y + P.y * B.x + A.x * B.y) -
           (B.x * A.y + B.y * P.x + A.x * P.y);
}

template<typename T>
vector<Point<T>> make_hull(const vector<Point<T>>& points, vector<Point<T>>& hull){
    vector<Point<T>> P(points);

    for (const auto& p : P){
        auto size = hull.size();

        while (size >= 2 and get_determinant(hull[size - 2], hull[size - 1], p) <= 0){
            hull.pop_back();
            size = hull.size();
        }

        hull.push_back(p);
    }

    return hull;
}

template<typename T> vector<Point<T>> make_monotone_chain(const vector<Point<T>>& points){
    vector<Point<T>> P(points);

    sort(P.begin(), P.end());

    vector<Point<T>> lower_hull, upper_hull;

    lower_hull = make_hull(P, lower_hull);

    reverse(P.begin(), P.end());

    upper_hull = make_hull(P, upper_hull);

    lower_hull.pop_back();
    lower_hull.insert(lower_hull.end(), upper_hull.begin(), upper_hull.end()); 

    return lower_hull;
}

int main(){
    vector<Point<ll>> P;
    ll x, y = 0;


    while(cin >> x >> y){
        P.push_back({x, y});
    }
    
    auto begin = std::chrono::high_resolution_clock::now();
    
    auto ch = make_monotone_chain<ll>(P);

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - begin);

    fprintf(stderr, "Time measured: %f seconds.\n", elapsed.count() * 1e-6);

    for (size_t i = 0; i < ch.size(); ++i)
        cout << ch[i].x << " " << ch[i].y << endl;

    return 0;
}
