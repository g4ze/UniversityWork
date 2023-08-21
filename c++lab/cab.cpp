#include <iostream>
#include <string>
//nilay gupta e22 cseu1318
using namespace std;
class Vehicle{
    public:
    string name;
};
class Driver{
    public:
    string name;
    Vehicle vehicle;
};
class Passenger{
    public:
    string name;
};
class Ride{
    public:
    Passenger passenger;
    Driver driver;
    int fare;
    string origin, destination;
};

void display(const Ride* ride){
    cout<<"Displaying info of Ride"<<endl;
    cout << "Displaying info of Ride" << endl;
    cout << "Passenger name: " << ride->passenger.name << endl;
    cout << "Driver name: " << ride->driver.name << endl;
    cout << "Preferred vehicle: " << ride->driver.vehicle.name << endl;
    cout << "Trip from" <<ride->destination<<"to"<<ride->origin<<endl;
    cout <<"Fare is"<<ride->fare;
}
void booking(const Driver* drivers){
    Ride ride;
    cout<<"Enter your name: "<<endl;
    cin>>ride.passenger.name;
    cout<<"Enter vehicle type B/C";
    string vehicle;
    cin>>vehicle;
    if(vehicle=="B"){
        for(int i=0;i<4;i++ ){
            if(drivers[i].vehicle.name=="Bike"){
                ride.driver=drivers[i];
                cout<<"enter destination:"<<endl;
                cin>>ride.destination;
                ride.fare=200;
                cout<<"Enter start: "<<endl;
                cin>>ride.origin;
                break;
            }
        }
    }
    if(vehicle=="C"){
        for(int i=0;i<4;i++ ){
            if(drivers[i].vehicle.name=="Car"){
                ride.driver=drivers[i];
                cout<<"enter destination:"<<endl;
                cin>>ride.destination;
                ride.fare=200;
                cout<<"Enter start: "<<endl;
                cin>>ride.origin;
                break;
            }
        }
    }
    display(&ride);

}


int main(){
    Driver drivers[4];//ramesh, suresh, deepak, nilay;
    drivers[0].name="Ramesh";
    drivers[0].vehicle.name="Bike";

    drivers[1].name="Suresh";
    drivers[1].vehicle.name="Bike";

    drivers[2].name="Deepak";
    drivers[2].vehicle.name="Car";

    drivers[3].name="Nilay";
    drivers[3].vehicle.name="Car";

    string input="";
    while(input!="exit"){

        booking(drivers);

        cin>>input;
    }

}

