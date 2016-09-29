//using postfix to calculate
#include "calculator.h"
bool isOperand(char ch) {
	return isalnum(ch);
}

// Function to verify whether a character is operator symbol or not.
bool isOperator(char ch) {
	if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^')
		return true;
	return false;
}

// Function to verify whether an operator is right associative or not.
int IsRightAssociative(char op) {
	if(op == '^') return true;
	return false;
}

// Function to get weight of an operator. An operator with higher weight will have higher precedence.
int GetOperatorWeight(char op)
{
	int weight = -1;
	switch(op) {
		case '+':
		case '-':
			weight = 1;
			break;

		case '*':
		case '/':
			weight = 2;
			break;

		case '^':
			weight = 3;
			break;
	}
	return weight;
}

// Function to perform an operation and return output.
int hasHigherPrecedence(char op1, char op2)
{
	int op1Weight = GetOperatorWeight(op1);
	int op2Weight = GetOperatorWeight(op2);

	// If operators have equal precedence, return true if they are left associative.
	// return false, if right associative.
	// if operator is left-associative, left one should be given priority.
	if(op1Weight == op2Weight)
	{
		if(IsRightAssociative(op1)) return false;
		else return true;
	}
	return op1Weight > op2Weight ?  true: false;
}

bool containsAlphaString(const string &str){
    for(int i = 0; i < str.size(); i++){
        if (isalpha(str[i])){
            return true;
        }
    }
    return false;
}

bool containsAlphaChar(const char* str){
    for(int i = 0; i < sizeof(str); i++){
        if (isalpha(str[i])){
            return true;
        }
    }
    return false;
}

bool indexInVector(vector<int> trackingIndex, int index){
    for(vector<int>::iterator it = trackingIndex.begin(); it != trackingIndex.end(); ++it){
        if (index == *it)
            return true;
    }
    return false;
}

float lookup(cell* cells, int index, int x, vector<int> trackingIndex){
    if (indexInVector(trackingIndex, index)){
        throw "Detect cyclic dependency\n";
    }
    vector<int>::iterator it = trackingIndex.begin();
    trackingIndex.insert ( it , index );
    if (cells[index].evaluate){
        return cells[index].value;
    }
    else {
        return calc(cells[index].equation, cells, x, trackingIndex);
    }
}

float calc(string postfix, cell* cells, int x, vector<int> trackingIndex)
{
    stack<float> number;
    char token[postfix.length()-1];
    int computeX, computeY, computeIndex;
    float op1, op2, result, lookupValue;
    char*  b;
    char first[2];
    bool singleNumber = true;


    for (int i = 0; i <=postfix.length()-1; i ++)
    {
        token[i]=postfix[i];
    }

    b = strtok(token, " ");
    
    while(b != NULL)
    {
        if (isOperand(b[0]))
        {
            if (isalpha(b[0])){
                try{
                    strncpy(first, b, 1);
                    char second[sizeof(b) - 1];
                    strncpy(second, b+1, sizeof(b) - 1);
                    computeX = atoi(second);
                    computeY = int(first[0])-65;
                    computeIndex = computeY * x + computeX - 1;
                    lookupValue = lookup(cells, computeIndex, x, trackingIndex);
                    number.push(lookupValue);
                } catch (const char* e) {
                    throw e;
                }
            } else {
                number.push(atoi(b));
            }
            b = strtok(NULL, " ");
        }

        else if (isOperator (b[0]))
        {
            singleNumber = false;
            switch(b[0])
            {
            case '+':
                {
                    op1 = number.top();
                    number.pop();
                    op2 = number.top();
                    number.pop();
                    result = op2+op1;
                    number.push(result);
                }
                break;

            case '-':
                {
                    op1 = number.top();
                    number.pop();
                    op2 = number.top();
                    number.pop();
                    result = op2-op1;
                    number.push(result);
                }
                break;

            case '*':
                {

                    op1 = number.top();
                    number.pop();

                    op2 = number.top();
                    number.pop();

                    result = op2*op1;
                    number.push(result);
                }
                break;

            case '/':
                {
                    op1 = number.top();
                    number.pop();
                    op2 = number.top();
                    number.pop();
                    result = op2/op1;
                    number.push(result);
                }
                break;
            }
            b = strtok(NULL, " ");
        }
       
    }
    if (singleNumber) {
        result = number.top();
        return result;
    }
   return result;

}

