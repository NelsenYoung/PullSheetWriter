// Nelsen Young
// 6/20/23
// Reads a csv

#include<stdio.h>
#include<string.h>
#include<string>
#include<iostream>
#include<stdbool.h>
#include <vector>
#include "coil.h"
using namespace std;

#define MAXCHAR 1000

int main(){
    FILE* fp;
    char row[MAXCHAR];
    char* token;
    coil coils[29];

    fp = fopen("Machine_Inventory.csv", "r");

    while(feof(fp) != true){
        fgets(row, MAXCHAR, fp);
        token = strtok(row, ",");
        int i = 0;

        while(token != NULL){
            int j = 0;
            switch (j)
            {
            case 0:
                coils[i].coil_num = atoi(token);
                printf("i: %d,", i);
                printf("j: %d,", j);
                printf("%d\n", coils[i].coil_num);
                break;
            case 1:
                coils[i].name = token;
                break;
            case 2:
                coils[i].item_num = atoi(token);
                break;
            case 3:
                coils[i].sold_num = atoi(token);
                break;
            default:
                break;
            }
            printf("token is Null");
            token = strtok(NULL, ",");
        }
    i++;
    }
    return 0;
}
