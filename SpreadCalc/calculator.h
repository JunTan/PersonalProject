#ifndef CALCULATOR_H_INCLUDED
#define CALCULATOR_H_INCLUDED
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib> // atoi
#include <stack>
#include <cctype>
#include <vector>
#include <exception>

using namespace std;

struct cell{
    float value;
    bool evaluate = false;
    string equation;
};

int GetOperatorWeight(char op);
int hasHigherPrecedence(char operator1, char operator2);
bool isOperator(char ch);
bool isOperand(char ch);
float calc(string postfix, cell*, int x, vector<int> trackingIndex);
bool containsAlphaString(const string &str);
bool containsAlphaChar(const char*);
float lookup(cell* cells, int index, int x, vector<int> trackingIndex);

#endif // CALCULATOR_H_INCLUDED
