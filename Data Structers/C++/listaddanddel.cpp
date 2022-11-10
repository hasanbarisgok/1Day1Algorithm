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
        this -> length = length;
        this -> a = new int [size];
    }
    
    //Constructor Method - Array is adding when starting
    Array(int size, int length, int arr[]){
        this -> size = size;
        this -> length = length;
        this -> a = new int[size];
        
        for(int i =0; i < length; i++){
            a[i] == arr[i];
        }
    }
    
    //Adding items to end of the list.
    void Append(int x){
        //If the list len < size, resume to adding process.
        if(this->length < this->size)
            a[this->length++] = x;
    }
    //List items is showing on the screen.
    void Display(){
        for (int i = 0; i < length; i++){
            cout << a[i] << " ";
        }
        cout << endl;
    }
    
    //Dynamic list is shooting from memory as deconstructor method.
    ~Array(){
        delete[] a;
    }
};

int main() {
    int a[] = {2,3,4,5,6};
    int size = sizeof(a) / sizeof(a[0]);
    
    //The arr is created from array class.
    Array arr(10,size,a);
    
    //Adding the value: "10" to end of the list.
    arr.Append(10);
    
    //The items which has entered has been showed on the screen:
    arr.Display();
    
    return 0;
}

#Hasan Baris GOK. C.E Student @ Osmaniye Korkut Ata Universtiy
#Thanks a lot Prof. H.T
