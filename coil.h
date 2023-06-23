#include <iostream>
#include <string>
using namespace std;

class coil
{
private:
public:
    std::string name;
    int coil_num;
    int sold_num;
    int item_num;

    coil();
    coil(std::string, int, int, int);

    void dump(std::string, int, int, int);
};

