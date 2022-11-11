#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm> //std::sort


struct DataType {
    int n;
    std::string str;
    std::string to_string() const {
        std::ostringstream oss;
        oss << n << ',' << str;
        return oss.str();
    }
};
std::ostream& operator<<(std::ostream& os, const DataType& data) {
    os << data.to_string();
    return os;
}

template<typename T> void sort(std::vector<T>& v) {
    std::sort(begin(v), end(v));
}

template<> void sort(std::vector<DataType>& v) {
    std::sort(begin(v), end(v), [](DataType& d1, DataType& d2)->bool { return d1.str < d2.str;});
}

template<typename Container> void fnPrintContainer(const Container& c) {
    for (const auto& e: c)
        std::cout << e << std::endl;
}

using namespace std;

int main()
{
    vector<int> vecInt = {3,5,2,1,7};
    vector<double> vecDbl = {1.,3.4, 2.1, 4, 0.3};
    vector<DataType> vecData = { {1, "a"}, {5, "d" }, {3, "b"}, {2, "c"} };

    sort(vecInt);
    // sort(vecDbl);
    // sort(vecData);

    fnPrintContainer(vecInt);
    // fnPrintContainer(vecDbl);
    // fnPrintContainer(vecData);
}