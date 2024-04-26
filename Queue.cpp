#include <iostream>
using namespace std;

#define MAX_SIZE 100

class Queue {
private:
    int front, rear;
    int arr[MAX_SIZE];

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isEmpty() {
        return (front == -1 && rear == -1);
    }

    bool isFull() {
        return (rear == MAX_SIZE - 1);
    }

    void insert(int value) {
        if (isFull()) {
            cout << "Queue Overflow\n";
            return;
        }
        if (isEmpty()) {
            front = rear = 0;
        } else {
            rear++;
        }
        arr[rear] = value;
        cout << "Inserted " << value << " into the queue\n";
    }

    void remove() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return;
        }
        int removed = arr[front];
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }
        cout << "Removed " << removed << " from the queue\n";
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty\n";
            return;
        }
        cout << "Queue elements: ";
        for (int i = front; i <= rear; ++i) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Queue queue;
    queue.insert(1);
    queue.insert(2);
    queue.insert(3);
    queue.display();
    queue.remove();
    queue.display();
    return 0;
}
