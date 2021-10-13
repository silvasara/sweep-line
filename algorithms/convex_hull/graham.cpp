/* 
Adaptação do código de Edson Alves, disponível em:
https://github.com/edsomjr/TEP/blob/master/Geometria_Computacional/slides/CH-1/graham.cpp
*/ 

#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using ll = long long int;

template<typename T> struct Point{
    T x, y;

    double get_distance(const Point& P) const{
        return hypot(x - P.x, y - P.y);
    }
};

template<typename T> T get_determinant(const Point<T>& P, const Point<T>& A, const Point<T>& B){
    return (P.x * A.y + P.y * B.x + A.x * B.y) -
           (B.x * A.y + B.y * P.x + A.x * P.y);
}

template<typename T> Point<T> get_pivot(vector<Point<T>>& P){
    for (size_t i = 1; i < P.size(); ++i)
        if (P[i].y < P[0].y or 
            (P[i].y == P[0].y and P[i].x > P[0].x))
                swap(P[0], P[i]);

    return P[0];
}

template<typename T> void sort_by_angle(vector<Point<T>>& P){
    auto P0 = get_pivot(P);

    sort(P.begin() + 1, P.end(),
        [&](const Point<T>& A, const Point<T>& B){
            // pontos colineares: escolhe-se o mais próximo do pivô
            if (get_determinant(P0, A, B) == 0) // se o get_determinante for 0, os pontos estão alinhados
                return A.get_distance(P0) < B.get_distance(P0);

            auto alfa = atan2(A.y - P0.y, A.x - P0.x);
            auto beta = atan2(B.y - P0.y, B.x - P0.x);

            return alfa < beta;
        }
    );
}

template<typename T> vector<Point<T>> make_convex_hull(const vector<Point<T>>& points){
    vector<Point<T>> P(points);
    auto N = P.size();

    // Corner case: com 3 vértices ou menos, P é o próprio convex hull
    if (N <= 3)
        return P;

    sort_by_angle(P);

    vector<Point<T>> ch;
    ch.push_back(P[N - 1]); // o primeiro ponto é igual ao último
    ch.push_back(P[0]);
    ch.push_back(P[1]);

    size_t i = 2;

    while (i < N) {
        auto j = ch.size() - 1;

        // se o get_determinante for positivo, a orientação se manteve
        if (get_determinant(ch[j - 1], ch[j], P[i]) > 0)
            ch.push_back(P[i++]);
        else
            ch.pop_back();
    }

    return ch;
}

int main(){
    vector<Point<ll>> P;
    ll x, y = 0;

    while(cin >> x >> y){
        P.push_back({x, y});
    }

    auto begin = std::chrono::high_resolution_clock::now();

    auto ch = make_convex_hull(P);

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - begin);

    fprintf(stderr, "Time measured: %f seconds.\n", elapsed.count() * 1e-6);


    for (size_t i = 0; i < ch.size(); ++i)
        cout << ch[i].x << " " << ch[i].y << endl;

    return 0;
}
