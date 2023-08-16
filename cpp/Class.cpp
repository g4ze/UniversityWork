#include <iostream>
using namespace std;
class Students{
    public:
    int id;
    string name;
    int grade;
    void setpassword(string pass){
        password=pass;
    }
    Students(){
        cout<<"Constructor called"<<endl;
    }
    void show(){
        cout<<"Id: "<<id<<endl;
        cout<<"Name: "<<name<<endl;
        cout<<"Grade: "<<grade<<endl;
    }
    private:
    string password;
    
};
int main(){
    Students s1;
    s1.id = 1;
    s1.name = "Rahul";
    s1.grade = 12;
    s1.show();
    return 0;
}