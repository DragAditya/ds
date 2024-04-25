#include <iostream>
using namespace std;
int findSmallest(int myarray[],int i);
int main()
{
    int myarray[10]={11,5,2,20,42,23,53,3,4,101,22};
    int pos,temp;
    cout<<"Unsorted List of elements "<<"\n";
    for(int i=0;i<10;++i)
    {
        cout<<myarray[i]<<" ";
    }
    cout<<"\n";
    for(int i=0;i<10;++i)
    {
        pos=findSmallest(myarray,i);
        temp=myarray[pos];
        myarray[pos]=myarray[i];
        myarray[i]=temp;
    }
    cout<<"\n"<<"Sorted list of elements is "<<"\n\n";
    for(int i=0;i<10;++i)
    {
        cout<<myarray[i]<<" ";
    }
    return 0;
}
int findSmallest(int myarray[],int i)
{
    int ele_small,position;
    ele_small=myarray[i];
    position=i;
    for(int j=i+1;j<10;++j)
    {
        if(myarray[j]<ele_small)
        {
            ele_small=myarray[j];
            position=j;
        }
    }
    return position;
}
