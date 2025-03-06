#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
    Node(int x, Node *n)
    {data=x; next=n;}
};
    
class LinkedList{
    private:
    Node* headNode;
    public: 
    LinkedList(){
        headNode = nullptr;
    }
    void Enqueue(int value){
    Node* newNode = new Node(value, nullptr);
    if(headNode == nullptr){
      headNode = newNode;
    }
    else{
      Node* temp = headNode;
      while (temp -> next != nullptr){
        temp = temp -> next; 
      }
      temp -> next = newNode;
    }
  }
    void Dequeue(){
        if(headNode == nullptr){
            cout << "Queue is already empty!";
    }
    else{
        Node *temp;
        temp = headNode;
        headNode = headNode->next;
        delete temp;
        };
    }
    
    void Top(){
        cout << headNode->data <<endl;
    }
  
  void Display(){
    Node* temp = headNode;
    while(temp != nullptr){
      cout << temp->data;
      temp = temp->next;
    }
    cout <<endl;
  }
  
  void isEmpty(){
    if(headNode->next == nullptr){
       cout << true << endl; 
    }
    else {
        cout << false << endl;
    }; 
  }
  void size(){
    int counter = 1;
    Node* temp = headNode;
    while(temp != nullptr){
      counter++;
      temp = temp->next;
    }
    cout << counter <<endl;
     
  }
};

int main()
{
    #include<new>

    LinkedList list;
    list.Enqueue(7);
    list.Enqueue(2);
    list.Enqueue(8);
    list.Enqueue(3);
    
    list.Display();
    
    list.Dequeue();
    
    list.Display();
    
    list.Top();
    
    list.isEmpty();
    
    list.size();
    
    return 0;
}

