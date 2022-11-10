#include <iostream>
#include <cstdlib>

using namespace std;

class Array{
private:
    int* a;
    int size;
    int length;

public:
    //Constructor Method
    Array(int size, int length){
        this -> size = size;
        this -> length =length;
        this -> a = new int[size];
    }
    //Changing index 
    void Set(int index, int x){
        if (index >=0 && index < length){
            a[index] = x;
        }
    }
    //Showing list's items 
    void Display(){
        for (int i = 0; i < length; i++){
            cout << a[i] << " ";
        }
        cout << endl;
    }
    //Dynamic List is shooting from memory as using Deconstructor Method.
    ~Array(){
        delete[] a;
    }
};

int main(){
    int size;
    cout << "Enter List's size";
    cin >> size;

    int length;
    cout << "Enter List's item length.";
    cin >> length;
    
    //Class Instance Has Created.
    Array arr(size, length);
    
    int value;
    for (int i = 0; i < length; i++){
        cin >> value;
        arr.Set(i,value);
    }
    //Showing items which are entered.
    arr.Display();
    
    return 0;
}
