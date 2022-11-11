#include <iostream>
#include <typeinfo>

using namespace std;

template <typename T> T fnSquare(const T& a) {
    return a*a;
}

template <typename T1, typename T2> T1 fnDivid(const T2& a, const T2& b) {
    return static_cast<T1>(a)/static_cast<T1>(b);
}

template <typename T, size_t N = 2> T fnPower(const T& a) { 
    T rst = 1;
    for (size_t i = 0; i < N; i++, rst*=a);
    return rst;
}

int main()
{
    auto v1 = fnSquare(5);
    cout << v1 << ',' << typeid(v1).name() << endl;
    auto v2 = fnSquare<double>(5.2);
    cout << v2 << ',' << typeid(v2).name() << endl;
    cout << fnDivid<double, int>( 3, 5) << endl;
    cout << fnPower<int>(5) << endl;
    cout << fnPower<int, 3>(5) << endl;
    
// 25,i
// 27.04,d
// 0.6
// 25
// 125
}