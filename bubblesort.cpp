#include <iostream>
using namespace std;
class BubbleSort
{
    int a[20],i,j,n,temp;
public:
    void getdata();
    void BSort();
    void display();
};
void BubbleSort::getdata()
{
    cout<<"Enter how many elements: ";
    cin>>n;
    cout<<"Enter elements: ";
    for(i=1;i<=n;i++)
    {
        cin>>a[i];
    }
}
void BubbleSort::BSort()
{
    for(i=1;i<=n-1;i++)
    {
        for(j=i+1;j<=n;j++)
        {
            if(a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}
void BubbleSort::display()
{
    cout<<"\nElements are Sorted using Bubble Sort in n";
    for(i=1;i<=n;i++)
    {
        cout<<a[i]<<" ";
    }
}
int main()
{
    BubbleSort b;
    b.getdata();
    b.BSort();
    b.display();
    return 0;
}￼Enter
