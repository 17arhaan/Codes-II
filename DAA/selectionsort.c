#include<stdio.h>

//swapping elements

void swap(int *x , int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

//main sorting function

void selectionsort (int arr[] , int n){
    
    int i;
    int j;
    int min_pos;

//finding minimum element

    for ( i=0; i<n-1; i++){
        min_pos = i;
        for ( j= i+1 ;j<n ; j++){
            if( arr[j] < arr[min_pos] )
            min_pos = j;

//swapping with the minimum element

            if(min_pos != i)
            swap(&arr[min_pos],&arr[i])
        }
    }
}
//display sorted array

void display(int arr[] , int size)