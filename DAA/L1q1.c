#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node* right;
    struct Node* left;
};
struct Node *parent = NULL;
struct Node* Create(struct Node *root, int data){
    if(root == NULL){
        root = (struct Node*) malloc(sizeof(struct Node));
        root->left = NULL;
        root->right = NULL;
        root->data = data;
        return root;
    }
    else{
        if(data < root->data && data != -1){
            root->left = Create(root->left, data);
        }
        else if(data > root->data && data != -1){
            root->right = Create(root->right, data);
        }
        else if(data == -1){
            return root;
        }
        else{
            printf("Duplicates Not Allowed\n");
        }
        return root;
    }
}
void InOrder(struct Node *root){
    if(root != NULL){
        InOrder(root->left);
        printf("%d ",root->data);
        InOrder(root->right);
    }
}
void PreOrder(struct Node *root){
    if(root != NULL){
        printf("%d ",root->data);
        PreOrder(root->left);
        PreOrder(root->right);
    }
}
void PostOrder(struct Node *root){
    if(root != NULL){
        PostOrder(root->left);
        PostOrder(root->right);
        printf("%d ",root->data);
    }
}
struct Node* Search(struct Node *root, int key){
    if(root == NULL){
        root = Create(root, key);
        return root;
    }
    else if(key > root->data){
        root->right = Search(root->right, key);
        return root;
    }
    else if(key < root->data){
        root->left = Search(root->left, key);
        return root;
    }
    else{
        printf("Key Found in BSTree");
        return root;
    }
}
void Print(struct Node *root){
    printf("\nInOrder Traversal ------> \n");
    InOrder(root);
    printf("\nPreOrder Traversal ------> \n");
    PreOrder(root);
    printf("\nPostOrder Traversal -------> \n");
    PostOrder(root);
}
int main(){
    int a, key;
    printf("Root Node (Enter -1 to Exit)");
    do
    {
        printf("Value for Node : ");
        scanf("%d",&a);
        if(a == -1){
            printf("All Current Nodes added\n");
        }
        parent = Create(parent, a);
    }while(a != -1);
    printf("Enter the Value of the Key : ");
    scanf("%d",&key);
    parent = Search(parent, key);
    Print(parent);
    return 0;
}