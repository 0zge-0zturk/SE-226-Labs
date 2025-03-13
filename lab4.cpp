#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int x)
    {data=x;}
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
        
    }
    void push(int x) {
        if (capacity-1 > num){
            Node* newNode = new Node(x);
            newNode->data = x;
            newNode->next = head;
            head = newNode;
            num++;
        }
        else{
            cout << "No capacity!" << endl;
            increaseCapacity();
        };
    }

    int pop() {
        if (isEmpty()) {
            cout<<"Stack is Empty!"<<endl;
            return 0;
        }
        
        cout<<"The popped element: "<< head->data <<endl;
        Node* temp = head;
        head = head->next;
        num--;
        return temp->data;
        delete head;
    }
    
    int peek() {
        cout << head->data << endl;
        return head->data;
    }
    
    

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity = capacity*2;
    }

    bool deleteElement(int val) {
        if(num <= 0){
            cout << "Stack is empty!" << endl;
        }
        else {
        Node* temp = head;
            while(temp != nullptr){
                temp = temp->next;
                
                if(val == temp->data){
                    temp = temp->next;
                    num--;
                    return temp->data;
                    delete temp;
                    return true;
                }
                else{
                    cout << "No value occurs!" << endl;
                    break;
                }
            }
        }
        return false; 
    }
};

int main() {
    #include<new>
    
    Stack stack(2);
    
    stack.push(8);
    stack.push(3);
    
    stack.push(4);
    stack.push(4);
    stack.peek();
    stack.deleteElement(4);
    stack.peek();
    

    return 0;
}
