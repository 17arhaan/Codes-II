#include<stdio.h>

void swap(int *x , int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

void selectionsort (int arr[] , int n){
    
    int i;
    int j;
    int min_pos;

    for ( i=0; i<n-1; i++){
        min_pos = i;
        for ( j= i+1 ;j<n ; j++){
            if( arr[j] < arr[min_pos] )
            min_pos = j;
        }
        if(min_pos != i)
        swap(&arr[min_pos],&arr[i]);
    }
}

void display(int arr[] , int size){
    for(int i=0 ; i < size ; i++){
        printf("%d",arr[i]);
    }
}

int main(){
    int arr[99];
    int size;
    printf("Enter the size of Array: ");
    scanf("%d",&size);
    for(int i = 0 ; i<size ; i++){
        printf("Enter Element {%d}: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("\nNormal Array --->\n");
    display(arr,size);
    selectionsort(arr,size);
    printf("\nSorted Array ---> \n");
    display(arr,size);
    return 0;
}