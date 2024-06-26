#include <iostream>
using namespace std;
void InsertionSort(int arr[], int n)
{
 int i, temp, j;
 for (i = 1; i < n; i++)
 {
  temp = arr[i];
  j = i - 1;
  while (j >= 0 && arr[j] > temp)
  {
   arr[j + 1] = arr[j];
   j = j - 1;
  }
  arr[j + 1] = temp;
 }
}
void PrintArray(int arr[], int n)
{
 int i;
 for (i = 0; i < n; i++)
  cout << arr[i] << " ";
 cout << endl;
}
int main()
{
 int arr[] = { 12, 11, 13, 5, 6 };
 int n = sizeof(arr) / sizeof(arr[0]);
 cout << "Before sorting array element:-\n";
 PrintArray(arr, n);
 InsertionSort(arr, n);
 cout << "After sorting array element:-\n";
 PrintArray(arr, n);
 return 0;
}
