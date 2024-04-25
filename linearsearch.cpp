#include <iostream>
using namespace std;
int main()
{
  int a[5]={10,20,30,40,50},item,i;
  cout<<"n Enter element for Search => ";
  cin>>item;
  while(i<5)
  {
    if(a[i]==item)
    {
      cout<<"\n Item Found";
      break;
    }
    i++;
  }
  if(i>=5)
  {
    cout<<"\n Item Not Found";
  }
  return 0;
}
