#include <iostream>
using namespace std;

#define MAX_SIZE 100

class Stack {
private:
    int top;
    int arr[MAX_SIZE];

public:
    Stack() {
        top = -1;
    }

    bool isEmpty() {
        return (top == -1);
    }

    bool isFull() {
        return (top == MAX_SIZE - 1);
    }

    void push(int value) {
        if (isFull()) {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++top] = value;
        cout << "Pushed " << value << " onto the stack\n";
    }

    void pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return;
        }
        int popped = arr[top--];
        cout << "Popped " << popped << " from the stack\n";
    }

    void display() {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return;
        }
        cout << "Stack elements: ";
        for (int i = 0; i <= top; ++i) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Stack stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.display();
    stack.pop();
    stack.display();
    return 0;
}￼Enter
