#include "calculator.h"
#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <cctype>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stdlib.h> 

using namespace std;

int main(){
    int x, y;
    cin >> x;
    cin >> y;
    //cells contains all the stdin input
    const int dim = x * y;
    cell* cells = new cell[dim];
    cin.ignore();
    string input;
    vector<int> trackingIndex;
    for (int i = 0; i < dim; i++){
        getline(cin, input);
        if (containsAlphaString(input)){
            cells[i].equation = input;
        } else {
            cells[i].evaluate = true;
            cells[i].value = calc(input, cells, x, trackingIndex);
        }
    }

    cout << "\n" << x << " " << y << endl;
    for (int i = 0; i < dim; i++){
        if (cells[i].evaluate) {
            cout << fixed;
            cout << setprecision(5) << cells[i].value << endl << endl;;
        } else {
            try{
                string equation = cells[i].equation;
                float result = calc(equation, cells, x, trackingIndex);
                cout << fixed;
                cout << setprecision(5) << result << endl;
                cells[i].value = result;
                cells[i].evaluate = true;
            } catch (const char* e){
                cout << e;
                delete [] cells;
                exit (EXIT_FAILURE);
            }

        }
    }
    delete [] cells;
    return 0;
}

