#include <iostream>
using namespace std;
int QPartition(int a[], int start, int end)
{
 int pivot = a[end];
 int i = (start - 1);
 for (int j = start; j <= end - 1; j++)
 {
  if (a[j] <= pivot)
  {
   i++;
   swap(a[i], a[j]);
  }
 }
 swap(a[i + 1], a[end]);
 return (i + 1);
}
void QuickSort(int a[], int start, int end)
{
 if (start < end)
 {
  int p = QPartition(a, start, end);
  QuickSort(a, start, p - 1);
  QuickSort(a, p + 1, end);
 }
}
void Printarr(int a[], int n)
{
 int i;
 for (i = 0; i < n; i++)
  cout << a[i] << " ";
 cout << "\n";
}
int main()
{
 int a[] = { 23, 8, 13, 28, 18, 26 };
 int n = sizeof(a) / sizeof(a[0]);
 cout << "Before sorting array elements are: \n";
 Printarr(a, n);
 QuickSort(a, 0, n - 1);
 cout << "After sorting array elements are: \n";
 Printarr(a, n);
 return 0;
}
