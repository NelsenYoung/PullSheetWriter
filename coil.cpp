#include "coil.h"

coil::coil(std::string _n, int _c, int _s, int _i){
    this->name = _n;
    this->coil_num = _c;
    this->sold_num = _s;
    this->item_num = _i;
}

coil::coil(){

}

void
coil::dump(std::string name, int coil_num, int item_num, int sold_num){
    printf("%d,", coil_num);
    printf("%s,", name.c_str());
    printf("%d,", item_num);
    printf("%d\n", sold_num);
}