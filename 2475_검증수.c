#include    <stdio.h>

int cal(int arr[]);

int main(){
    int arr[5];
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", arr[i]);
    }

    printf("%d", cal(arr));    
}

int cal(int arr[]){
    int result = 0;
    for (int i = 0; i < 5; i++)
    {
            result += (arr[i]*arr[i]);
    }
    
    result = result % 10;
    return result;
}